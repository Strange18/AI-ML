from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    objects = tasks.objects.all()
    form = task_add()
    if (request.method == 'POST'):
        form = task_add(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    return render (request,'home.html',{'tasks':objects,'form':form})