from django.db import models

# Create your models here.
class OptionSet(models.Model):
	name = models.CharField(max_length=30)
	limit = models.IntegerField()

class Option(models.Model):
	name = models.CharField(max_length=30)
	option_set = models.ForeignKey('OptionSet')