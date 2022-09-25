from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

#Code taken from tutorial - ** (see references)

# *** Register view
# Code taken form turtorial [6] (see references)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #Checking if form is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #Showing sucess message to user
            messages.success(request, 'Your account has been crearted! You can now log in')
            #Redirecting to login page
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# *** Profile view, user has to be logged in to see profile
# Code taken form turtorial [9] (see references)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        #Checking if both user informaiton and profile informationa re correct
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            #Showing sucess message to user 
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)