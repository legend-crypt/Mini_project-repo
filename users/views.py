from django.shortcuts import render, redirect
from .forms import *



def homeView(request):
    return render(request, 'home.html')


def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authencate(username=username, password=password)
            if user is not None:
                login(request, user)
                return ('profile')
    form = SignUpForm()
    return redirect(request, 'signup.html', {'form': form})

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


def profileView(request):
    if request.method == 'GET':
        details = Profile.objects.all()
    return render(request, 'profile.html', {details: details})        
