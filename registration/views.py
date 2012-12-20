# Create your views here.
from moderator.models import *
from moderator.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request, registration_id):
	options_set = OptionSet.objects.get(pk=int(registration_id))
	
	return render_to_response('index2.html', {'set': options_set} ,context_instance=RequestContext(request))

def register(request, registration_id, option_id):
	o_set = OptionSet.objects.get(pk=int(registration_id))
	option = None
	form = ChoiceForm()
	
	try:
		option = o_set.option_set.all()[int(option_id) - 1]
	except:
		pass

	return render_to_response('register.html', {'set': o_set, 'option': option, 'form': form} ,context_instance=RequestContext(request))	

def save_choice(request, registration_id, option_id):
	o_set = OptionSet.objects.get(pk=int(registration_id))
	option = None
	form = ChoiceForm()
	
	try:
		option = o_set.option_set.all()[int(option_id) - 1]
	except:
		pass

	if request.COOKIES.has_key('close_registration'):
	    return render_to_response('already.html', context_instance=RequestContext(request))
	else:
		response = HttpResponse( 'choice_maker' )
  		response.set_cookie( 'close_registration', 'yes')

  		if (request.POST):
  			form = ChoiceForm(request.POST)
  			if (form.is_valid()):
  				o=form.save(commit=False)
  				o.option_id = option_id
  				o.save()
  				return render_to_response('index.html', {'set': options_set} , context_instance=RequestContext(request))