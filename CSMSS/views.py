from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from django.urls import reverse as _

def home(request):
    return render(request, 'home.html')



def user_login(request):  # Changed the function name to avoid conflicts
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                auth_login(request, user)  # Use the imported auth_login
                if user.is_student:
                    return redirect('student:home')  # Ensure this URL name exists
                elif user.is_teacher:
                    return redirect('teacher:home')  # Ensure this URL name exists
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
