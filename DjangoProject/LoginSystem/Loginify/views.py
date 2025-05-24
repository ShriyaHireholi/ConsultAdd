from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .serializers import UserSerializer
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

def get_users(request):
    email = request.GET.get('email')
    if email:
        try:
            user = User.objects.get(email=email)
            return JsonResponse({'user': {'username': user.username, 'email': user.email}})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        users = User.objects.all().values('username', 'email')
        return JsonResponse({'users': list(users)})

@csrf_exempt
@api_view(['PATCH'])
def update_user(request, username=None):
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'User updated successfully',
                'user': {
                    'username': user.username,
                    'email': user.email
                }
            })

@csrf_exempt
def delete_user(request):
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    user.delete()
    return JsonResponse({
        'message': 'User deleted successfully',
        'user': {
            'username': user.username,
            'email': user.email
        }
    })