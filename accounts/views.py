from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django import forms
# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # Possible to do it in forms.py level
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # verify valid username and password
        user = authenticate(username=username, password=password)
        if user == None:
            raise forms.ValidationError("Username or password not valid")
            return redirect("/login")
        login(request,user)

        return redirect("/")
    return render(request, "accounts/login_form.html", {'form':form})
