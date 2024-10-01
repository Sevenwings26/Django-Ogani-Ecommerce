from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()
    
    context = {
        'form':form
    }
    return render(request, 'registration/register.html', context)