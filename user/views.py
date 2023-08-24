from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm, UserUpdateForm, ProfileUpdateForm

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

def profile_update(request):
    if request.method=="POST":
        user_form =UserUpdateForm(request.POST, instance=request.user)
        profile_form =ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('user-profile')
            
    else:
        user_form =UserUpdateForm(instance=request.user)
        profile_form =ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        
    }
    return render(request, 'user/profile_update.html', context)
    