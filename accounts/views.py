from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def password_reset_simple(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("password_reset")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User not found")
            return redirect("password_reset")

        user.set_password(password1)
        user.save()
        messages.success(request, "Password updated successfully")
        return redirect("login")

    return render(request, "accounts/password_reset_simple.html")