from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() ## if valid save to data base
            # print("Valid")
            username=form.cleaned_data.get('username') ## Get user name
            email=form.cleaned_data.get('email')


            messages.success(request,f"Acount Created Successfully!")
            return redirect('login')

    else:
        form=UserRegisterForm()

    return render(request , 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, "users/profile.html")