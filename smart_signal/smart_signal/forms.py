from django import forms
from .models import CompanyDetails
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

class CompanyDetailsForm(forms.ModelForm):
    class Meta():
        model = CompanyDetails
        fields = ('company_name','company_url','company_logo','contact_details')
