from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm

# 고정 계정 정보 (슈퍼 유저)
FIXED_USERNAME = "superuser"
FIXED_PASSWORD = "1234"

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 폼은 그대로 받아오되, 입력값은 무시하고 고정 계정 사용
            user, created = User.objects.get_or_create(username=FIXED_USERNAME)

            if created:
                user.set_password(FIXED_PASSWORD)
                user.is_staff = False  # admin 권한 안 주는 걸 권장
                user.save()

            user = authenticate(request, username=FIXED_USERNAME, password=FIXED_PASSWORD)
            if user is not None:
                login(request, user)
                return redirect('chatbot:chat_interface')
            else:
                form.add_error(None, '로그인 실패: 고정 계정 인증 실패')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')