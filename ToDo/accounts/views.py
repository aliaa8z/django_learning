from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'User register successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User login successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'User logout successfully', 'success')
    return redirect('home')