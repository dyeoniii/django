from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # 비밀번호 길이, 비밀번호 확인 일치, 필수 입력 필드 확인, 이메일 형식 검증
        if form.is_valid():
            form.save()
            # 유효성 검증 한 번 더 실행
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
