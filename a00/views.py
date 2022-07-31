from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.validators import validate_email

from .forms import SigninForm, SignupForm

def index(request):
    return render(request, 'DjangoApps/templates/a00/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            if data['password'] != data['password2']:
                form = SignupForm()
                context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

            try:
                validate_email(data['username'])
            except: #ValidationError
                form = SignupForm()
                context = {'message':'이메일 형식이 바르지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

            if data['password'] == data['password2']:
                user = User.objects.create_user(username=data['username'], password=data['password'])
                user = authenticate(request, username=data['username'], password=data['password'])
                login(request, user)
                return redirect('a00:index')

            else:
                form = SignupForm()
                context = {'message':'이미 가입한 아이디입니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

    else:
        form = SignupForm()
        return render(request, 'DjangoApps/templates/a00/signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            try:
                validate_email(data['username'])
            except: #ValidationError
                form = SigninForm()
                context = {'message':'이메일 형식이 바르지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signin.html', context)

            try:
                user = User.objects.get(username=data['username'])
            except: #ObjectDoesNotExist
                form = SigninForm()
                context = {'message':'가입되어 있지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signin.html', context)

            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return redirect('a00:index')
            else:
                form = SigninForm()
                context = {'message':'비밀번호를 확인해주세요', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signin.html', context)

    else:
        form = SigninForm()
        return render(request, 'DjangoApps/templates/a00/signin.html', {'form':form})