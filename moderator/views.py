from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from moderator.forms import *

def index(request):
    if request.user.is_authenticated():
        is_logged_in = True
        registrations = request.user.optionset_set.all()
    else:
        is_logged_in = False
        registrations = {}

    return render_to_response('index.html', {'is_logged_in': is_logged_in, 'registrations' : registrations},
        context_instance=RequestContext(request)
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/moderator/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/signup.html", {
        'form': form }, context_instance=RequestContext(request) )

@login_required(login_url='/moderator/login/')
def new_optionset(request):
    if request.method == 'POST':
        form = OptionSetForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            limit = request.POST['limit']
            limit = int(limit)
            optionset = request.user.optionset_set.create(name=name, limit=limit)
            optionset_id = optionset.id

            return HttpResponseRedirect("/moderator/optionset/" + str(optionset_id) + "/add_options")
    else:
        form = OptionSetForm()
    return render_to_response("optionset/new.html", {
        'form': form }, context_instance=RequestContext(request) )

@login_required(login_url='/moderator/login/')
def add_options(request, optionset_id):
    if int(optionset_id) in map(OptionSet.ids, request.user.optionset_set.all()):
        optionset = OptionSet.objects.get(pk=int(optionset_id))
        if request.method == 'POST':
            formset = OptionFormset(request.POST)
            if formset.is_valid():
                for form in formset.cleaned_data:
                    if form.has_key('name'):
                        option = Option(name = form['name'])
                    else:
                        option = Option(name = "Default choice")
                    option.option_set = optionset
                    option.save()

                request.flash['url'] = "URL to your registration: http://localhost:8000/registration/" + str(optionset_id)
                return HttpResponseRedirect("/moderator/")

        else:
            formset = OptionFormset()
            return render_to_response("optionset/add_options.html", {
                'formset': formset, 'optionset_id' : optionset_id }, context_instance=RequestContext(request) )
    else:
        request.flash['notice'] = "You don't have access to this optionset!"
        return HttpResponseRedirect("/moderator/")