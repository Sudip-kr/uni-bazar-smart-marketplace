from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# ✅ SIGNUP
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   # signal creates profile
            login(request, user)
            return redirect('core:home')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


# ✅ PROFILE
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


# ✅ EDIT PROFILE
@login_required
def edit_profile_view(request):
    return render(request, 'accounts/edit_profile.html')