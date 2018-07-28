from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    q = request.POST
    username = q.get('username')
    password = q.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
             login(request, user)
             return redirect('/products/')
    return render(request, 'loginpage.html')


def logout_view(request):
    logout(request)
    return redirect('/')

