from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm

# 고정 계정 정보 (슈퍼 유저)
FIXED_USERNAME = "superuser"
FIXED_PASSWORD = "1234"

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if (form.cleaned_data['username'] == FIXED_USERNAME and 
                form.cleaned_data['password'] == FIXED_PASSWORD):
                user, created = User.objects.get_or_create(username=FIXED_USERNAME)
                if created:
                    user.set_password(FIXED_PASSWORD)
                    user.save()

                user = authenticate(request, username=FIXED_USERNAME, password=FIXED_PASSWORD)
                if user is not None:
                    login(request, user)
                    return redirect('chatbot:chat_interface')
            else:
                # form.add_error(None, '고정된 사용자명과 비밀번호를 입력하세요.')
                messages.error(request, '아이디와 비밀번호를 확인하세요.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')