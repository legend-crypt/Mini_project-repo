from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json




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
                return redirect('profile')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'signin.html')


def logoutView(request):
    logout(request)
    return redirect('home')

@login_required()
def profileView(request):
    import requests
    if 'location' in request.GET:
        city = request.GET.get('location')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'b0619da772219bc7279a401ff34bfa93'}"
        

        # demonstrate how to use the 'params' parameter:
        x = requests.get(url)

        #Converts response object to dictionary
        x = x.json()
        print(x)

        context = {
            'weather_condition': f"Weather Condition - {x['weather'][0]['main'].upper()}",
            'weather_description': f"Weather Description - {x['weather'][0]['description'].upper()}",
            'country': f"Country - {x['sys']['country'].upper()}",
            'city':  f"City - {x['name'].upper()}",
            'temp':  f"{x['main']['temp']}",
            'base': f"Base - {x['base'].upper()}"
        }
        current_temp = float(context['temp']) / 10
        if current_temp > 25:
            outcome = Description.objects.get(id=1)
        else: 
            outcome = Description.objects.get(id=2)


        return render(request, 'profile.html', {'context': context, 'outcome': outcome})
    return render(request, 'profile.html')

        
