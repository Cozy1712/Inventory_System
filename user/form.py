from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#  creating an email field to the usercreation form
class CreateUserForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2' ]