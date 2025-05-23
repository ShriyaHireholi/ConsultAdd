from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import User

# Create your views here.
def index(request):
    return render(request, "Loginify/index.html")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    
    return render(request, 'Loginify/signup.html')

def login_view(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_object = User.objects.get(email=email, password=password)
            if user_object:
                return redirect('index')
            else:
                return HttpResponse("Invalid Credentials")
        except:
            return HttpResponse("Invalid Credentials")
        
    return render(request, "Loginify/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

