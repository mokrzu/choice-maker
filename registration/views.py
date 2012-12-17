# Create your views here.
from moderator.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request, registration_id):
	options_set = OptionSet.objects.get(pk=int(registration_id))
	
	return render_to_response('index2.html', {'set': options_set} ,context_instance=RequestContext(request))
