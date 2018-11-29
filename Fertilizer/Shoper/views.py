from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import ShoperForm, MyRegistrationForm, ShoperSignup
from django.http import HttpResponseRedirect
from django.contrib import auth


#login form in shoper

def shoper_login(request):
    if request.method == 'POST':
        form = ShoperForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user not in None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated''successfuly')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = ShoperForm()
    return render(request, 'Shoper/login.html', {'form' : form})



def signup(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ShoperForm')
    else:
        form = MyRegistrationForm()
    return render(request, 'Shoper/signup.html', {'form': form})

def signup1(request):
    if request.method == 'POST':
        form = ShoperSignup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ShoperForm')
    else:
        form = ShoperSignup()
    return render(request, 'Shoper/signup1.html', {'form': form})