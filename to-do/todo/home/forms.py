from .models import *
from django import forms
from django.db.models import fields



class task_add(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['name']
