from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.
class OptionSet(models.Model):
    name = models.CharField(max_length=40)
    limit = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name + ' (' + str(self.id) + ')'

    def ids(object):
        return object.id
    ids = staticmethod(ids)


class Option(models.Model):
    name = models.CharField(max_length=40)
    option_set = models.ForeignKey('OptionSet')

    def __unicode__(self):
        return self.name

class Choice(models.Model):
    author = models.CharField(max_length=30)
    magic_word = models.CharField(max_length=30)
    option = models.ForeignKey('Option')

    def __unicode__(self):
        return self.author
