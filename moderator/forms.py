from django.forms.models import formset_factory
from django.forms import ModelForm
from models import *
from django import forms

class OptionForm(ModelForm):
    class Meta:
        model = Option
        exclude = ('option_set')

OptionFormset = formset_factory(OptionForm, extra=2)

class OptionSetForm(ModelForm):
    class Meta:
        model = OptionSet
        exclude = ('user',)