from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        # user = User model, django.contrib.auth.models.User =
        if user is not None:
            return user
        else:
            raise forms.ValidationError("Incorrect username or password")


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password confirmation'}))

    class Meta:
        model = User
        # Specify the fields to use with 'clean'
        fields = ['username','email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        # The iexact lookup is used to get records with a specified value. The iexact lookup is case insensitive
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean(self):
        data = self.cleaned_data
        # data = dictionary
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        # The iexact lookup is used to get records with a specified value. The iexact lookup is case insensitive
        if qs == None:
            raise forms.ValidationError("Email is taken")
        return email
