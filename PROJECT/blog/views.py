from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

from .form import CreateUserForm

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte de ' + user + ' inscrit')
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profil')
        else:
            messages.info(request, "Nom d'utilisateur ou mot de passe incorrect")
        
    context = {}
    return render(request, 'accounts/login.html', context)

def profilPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=request.user)
        user = request.user
        u = User.objects.get(username=user)
        u.email = request.POST.get('email')
        user.email = u.email
        u.save()
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)
