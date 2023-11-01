from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     password = forms.PasswordInput(attrs={'placeholder': 'Your password'})
#     password2 = forms.PasswordInput(attrs={'placeholder': 'Your password confirmation'})
