from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def logout_view(request):
    # form
    logout(request)
    return redirect("/login")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.cleaned_data
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login_form.html", {'form':form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.cleaned_data
            password = make_password(user['password'])
            new_user = User(username=user['username'], email=user['email'],password=password)
            new_user.save()
            # Commit = False doesn't save the
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register_form.html", {'form': form})
