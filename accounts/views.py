from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django import forms
# Create your views here.

def logout_view(request):
    # form
    logout(request)
    return redirect("/login")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # Possible to do it in View
        #username = form.cleaned_data.get('username')
        #password = form.cleaned_data.get('password')
        # verify valid username and password
        #user = authenticate(username=username, password=password)
        user = form.cleaned_data
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login_form.html", {'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        print(form.cleaned_data)
    return render(request, "accounts/register_form.html", {'form': form})
