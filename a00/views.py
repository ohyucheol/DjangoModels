from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email

from .forms import SigninForm, SignupForm, ChangePasswordForm, ChangeUsernameForm

def index(request):
    return render(request, 'DjangoApps/templates/a00/index.html')

def signout(request):
    logout(request)
    return render(request, 'DjangoApps/templates/a00/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        #checking all items are filled
        if form.is_valid():
            data = form.cleaned_data

            #checking password is correct
            if data['password'] != data['password2']:
                form = SignupForm()
                context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

            #checking email is correct
            try:
                validate_email(data['username'])
            except: #ValidationError
                form = SignupForm()
                context = {'message':'이메일 형식이 바르지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

            #checking user is already exist
            try:
                user = User.objects.create_user(username=data['username'], password=data['password'])
            except:
                form = SignupForm()
                context = {'message':'이미 가입한 이메일입니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/signup.html', context)

            #pass all conditions
            user = authenticate(request, username=data['username'], password=data['password'])
            login(request, user)
            return redirect('a00:index')

        #when some items are not filled
        else:
            form = SignupForm()
            context = {'message':'이메일과 비밀번호를 입력해주세요', 'form':form}
            return render(request, 'DjangoApps/templates/a00/signup.html', context)

    #when user visits signup page
    else:
        form = SignupForm()
        return render(request, 'DjangoApps/templates/a00/signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)

        #checking all items are filled
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
            context = {'message':'이메일과 비밀번호를 입력해주세요', 'form':form}
            return render(request, 'DjangoApps/templates/a00/signin.html', context)
    else:
        form = SigninForm()
        return render(request, 'DjangoApps/templates/a00/signin.html', {'form':form})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('a00:signin')

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] != data['password2']:
                form = ChangePasswordForm()
                context = {'message':'새로운 비밀번호가 서로 일치하지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/change-password.html', context)

            user = authenticate(request, username=request.user.username, password=data['current_password'])
            
            if user is not None:
                user.set_password(data['password'])
                user.save() 
                login(request, user)
                return redirect('a00:index')
            else:
                context = {'message':'현재 비밀번호가 일치하지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/change-password.html', context)

        else:
            form = ChangePasswordForm()
            context = {'message':'비밀번호를 입력해주세요', 'form':form}
            return render(request, 'DjangoApps/templates/a00/change-password.html', context)

    else:
        form = ChangePasswordForm()
        return render(request, 'DjangoApps/templates/a00/change-password.html', {'form':form})


def change_username(request):
    if not request.user.is_authenticated:
        return redirect('a00:signin')

    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            try:
                validate_email(data['username'])
            except: #ValidationError
                form = ChangeUsernameForm()
                context = {'message':'이메일 형식이 바르지 않습니다', 'form':form}
                return render(request, 'DjangoApps/templates/a00/change-username.html', context)

            user = authenticate(request, username=request.user.username, password=data['password'])

            if user is not None:
                user.username = data['username']
                user.save()
                login(request, user)
                return redirect('a00:index')
            else:
                form = ChangeUsernameForm()
                context = {'message':'비밀번호를 확인해주세요', 'form':form}
                return render(request, 'DjangoApps/templates/a00/change-username.html', context)

        else:
            form = ChangeUsernameForm()
            context = {'message':'비밀번호를 입력해주세요', 'form':form}
            return render(request, 'DjangoApps/templates/a00/change-username.html', context)

    else:
        form = ChangeUsernameForm()
        return render(request, 'DjangoApps/templates/a00/change-username.html', {'form':form})

