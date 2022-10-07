from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from myapp.forms import CreateUserForm
# Create your views here.


def register(request):
    form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html',context)