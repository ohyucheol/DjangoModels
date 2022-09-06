import os, json

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .forms import CreateUserForm, UpdateUsernameForm,UpdateEmailForm, \
                    UpdatePasswordForm, UpdateBannedKeywordForm, LoginUserForm

# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/A01/about.html"

class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'DjangoApps/templates/A01/create-user.html'
    success_url = '/A01/'

    def form_invalid(self, form):
        # field validation error를 처리한다.
        for f in self.form_class.Meta.fields:   # form의 모든 field에 대하여
            if form.has_error(f):               # validation error가 있는지 확인한 후 있으면
                for err in form.errors[f]:      # (이 loop은 html 요소를 제거하기 위한 것이다.)
                    context = {'message': err, 'form':form} # 그 error에 관한 messages를 포함하여 render 한다.
                    return render(self.request, self.template_name, context)

        # non-field validation error 및 기타 error를 처리한다.
        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        # 기본적인 validation을 통과한 field를 대상으로 추가 검증을 수행한다.
        data = form.cleaned_data

        # if User.objects.filter(email=data['email']):
        #     context = {'message':'이미 사용중인 이메일입니다', 'form':form}
        #     return render(self.request, self.template_name, context)

        if data['password1'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, self.template_name, context)

        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = template_name = 'DjangoApps/templates/A01/login-user.html'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        # non-field validation error 및 기타 error를 처리한다.
        for err in form.errors['__all__']:
            context = {'message': err, 'form':form}
            return render(self.request, self.template_name, context)

class LogoutUserView(LogoutView):
    form_class = LoginUserForm
    template_name = 'DjangoApps/templates/A01/login-user.html'

class PersonalUserView(TemplateView):
    template_name = "DjangoApps/templates/A01/personal-user.html"

    def get_context_data(self, **kwargs):
        page_owner = User.objects.get(username=kwargs['username'])
        self.extra_context = {'page_owner' : page_owner}
        kwargs.update(self.extra_context)
        
        return kwargs

class UpdateUsernameView(UpdateView):
    model = User
    form_class = UpdateUsernameForm
    initial = {'username' : ''}
    template_name = "DjangoApps/templates/A01/update-username.html"
    success_url = '/A01/'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

class UpdateEmailView(UpdateView):
    model = User
    form_class = UpdateEmailForm
    initial = {'email' : ''}
    template_name = "DjangoApps/templates/A01/update-email.html"
    success_url = '/A01/'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

class UpdatePasswordView(UpdateView):
    model = User
    form_class = UpdatePasswordForm
    template_name = 'DjangoApps/templates/A01/update-password.html'
    success_url = '/A01/'

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        data = form.cleaned_data

        if data['password1'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, self.template_name, context)

        user = authenticate(self.request, username=self.request.user.username, password=data['password'])
        
        if user is None:
            context = {'message':'현재 비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, self.template_name, context)

        #모든 추가 검증을 통과한 경우
        user.set_password(data['password1'])
        user.save() 
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class UpdateBannedKeywordView(FormView):
    form_class = UpdateBannedKeywordForm
    template_name = 'DjangoApps/templates/A01/update-banned-keyword.html'
    success_url = '/A01/update-banned-keyword'

    def get_initial(self):
        # banned.json의 구조
        # {
        # "full": ["alfa", "bravo", "charile"],
        # "part": ["delta", "echo", "foxtrot"]
        # }
        path = os.path.dirname(__file__) + '/banned.json'
        file = open(path)
        banned_keyword = json.load(file)

        full = '' ; part = ''

        for b in banned_keyword['full']:
            full = full + b + ' '

        for b in banned_keyword['part']:
            part = part + b + ' '

        self.initial['full'] = full
        self.initial['part'] = part

        return self.initial

    def form_invalid(self, form):
        for f in self.form_class.Meta.fields:
            if form.has_error(f):
                for err in form.errors[f]:
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        data = form.cleaned_data #string

        banned_keyword = {}
        banned_keyword['full'] = data['full'].split()
        banned_keyword['part'] = data['part'].split()

        path = os.path.dirname(__file__) + '/banned.json'
        file = open(path, 'w')

        json.dump(banned_keyword, file)

        return HttpResponseRedirect(self.success_url)