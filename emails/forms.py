from django import forms
from .models import EmailEntry

class EmailEntryForm(forms.ModelForm):
    class Meta: # How to describe the from we're using
        model = EmailEntry # Declare the model which this form is using
        fields = ['email']
    def clean_email(self): # clean_<fieldName>
        email = self.cleaned_data.get('email')
        # if email.endswith("gmail.com"):
        #     raise forms.ValidationError(('Invalid email'), code='invalid')

        # The iexact lookup is case insensitive.
        qs = EmailEntry.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('Thank you, you have already registered')
        return email
