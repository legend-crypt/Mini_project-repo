from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect





def homeView(request):
    return render(request, 'home.html')


@csrf_exempt
def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
                auth_login(request, user)
                messages.success(request, "login successful")
                return redirect('home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'signin.html')


def logoutView(request):
    logout(request)
    return redirect('home')

@login_required()
def profileView(request):
    if request.method == 'GET':
        try:
            details = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            details = None
        return render(request, 'profile.html', {'details': details})
    return render(request, 'profile.html')

        
