from .forms import CreateUserForm, UpdateUsernameForm,UpdateEmailForm, UpdatePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

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
                for err in form.errors[f]:      # 그 error에 관한 messages를 포함하여 render 한다.
                    context = {'message': err, 'form':form}
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

class UpdateUsernameView(UpdateView):
    model = User
    form_class = UpdateUsernameForm
    initial = {'username' : ''}
    template_name = "DjangoApps/templates/A01/update-username.html"
    success_url = '/A01/'

    def form_invalid(self, form):
        # field validation error를 처리한다.
        for f in self.form_class.Meta.fields:   # form의 모든 field에 대하여
            if form.has_error(f):               # validation error가 있는지 확인한 후 있으면
                for err in form.errors[f]:      # 그 error에 관한 messages를 포함하여 render 한다.
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        # non-field validation error 및 기타 error를 처리한다.
        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

class UpdateEmailView(UpdateView):
    model = User
    form_class = UpdateEmailForm
    initial = {'email' : ''}
    template_name = "DjangoApps/templates/A01/update-email.html"
    success_url = '/A01/'

    def form_invalid(self, form):
        # field validation error를 처리한다.
        for f in self.form_class.Meta.fields:   # form의 모든 field에 대하여
            if form.has_error(f):               # validation error가 있는지 확인한 후 있으면
                for err in form.errors[f]:      # 그 error에 관한 messages를 포함하여 render 한다.
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        # non-field validation error 및 기타 error를 처리한다.
        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

class UpdatePasswordView(UpdateView):
    model = User
    form_class = UpdatePasswordForm
    template_name = 'DjangoApps/templates/A01/update-password.html'
    success_url = '/A01/'

    def form_invalid(self, form):
        # field validation error를 처리한다.
        for f in self.form_class.Meta.fields:   # form의 모든 field에 대하여
            if form.has_error(f):               # validation error가 있는지 확인한 후 있으면
                for err in form.errors[f]:      # 그 error에 관한 messages를 포함하여 render 한다.
                    context = {'message': err, 'form':form}
                    return render(self.request, self.template_name, context)

        # non-field validation error 및 기타 error를 처리한다.
        context = {'message': form.errors, 'form':form}
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        # 기본적인 validation을 통과한 field를 대상으로 추가 검증을 수행한다.
        data = form.cleaned_data

        if data['password1'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, self.template_name, context)

        user = authenticate(self.request, username=self.request.user.username, password=data['password'])
        
        if user is None:
            context = {'message':'현재 비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, self.template_name, context)

        #모든 검증을 통과한 경우
        user.set_password(data['password1'])
        user.save() 
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)







