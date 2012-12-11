from django.db import models

# Create your models here.
class OptionSet(models.Model):
	name = models.CharField(max_length=40)
	limit = models.IntegerField()

class Option(models.Model):
	name = models.CharField(max_length=40)
	option_set = models.ForeignKey('OptionSet')

class Choice(models.Model):
	author = model.CharField(max_length=30)
	magic_word = model.CharField(max_length=30)
	option = models.OneToOneField('Option')