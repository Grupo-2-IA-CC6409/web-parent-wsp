from ast import If
from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import CreateUserForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
        else :

            messages.error(request, "Error en el registro")
    else:
        form = CreateUserForm()
    context = { 'form' : form }
    return render(request, 'register.html', context)