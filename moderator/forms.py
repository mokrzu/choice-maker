from django.forms.models import modelformset_factory
from models import Option

OptionFormSet = modelformset_factory(Option)