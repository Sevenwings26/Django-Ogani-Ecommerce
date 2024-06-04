from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.

def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # authentication and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully created an account.")
            return redirect('index')
        else:
            form = SignUpForm()
    return render(request, "nav/register.html", {'form':form})
