from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm

# Create your views here.
# creating registraion for user using FBV
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST) #the user detail
        if form.is_valid(): #check for the form validation
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
        
    context = {
        'form' : form,
    }
    return render(request, 'user/register.html', context)
 
# creating profile page
def profile(request):
    return render(request, 'user/profile.html')