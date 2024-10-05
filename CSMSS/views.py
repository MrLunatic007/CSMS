from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm  # Assuming you have a LoginForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login/login.html')