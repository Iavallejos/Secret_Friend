from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, primary_key=True)

    def __str__(self):
        return self.email


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        labels = {
            'name': _('Full Name'),
            'email': _('Email'),
        }


class Pair(models.Model):
    userEmail = models.EmailField(unique=True, primary_key=True)
    pairEmail = models.EmailField(unique=True)
