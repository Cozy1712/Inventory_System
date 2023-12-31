from django import forms 
from .models import Profile
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
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image',]