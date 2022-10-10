
from ast import If
from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from myapp.forms import CreateUserForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    context = {
        'form': CreateUserForm
    }
    if request.method == 'POST':
        form = CreateUserForm(data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado')
            context['form'] = form
            return redirect('login')
        context['form'] = form
    
    return render(request, 'register.html', context)

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
