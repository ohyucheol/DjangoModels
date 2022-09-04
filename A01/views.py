from .forms import UserCreateForm
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/A01/about.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'DjangoApps/templates/A01/user-form.html'
    success_url = '/A01/'

    def form_invalid(self, form):
        # field validation error를 처리한다.
        for f in self.form_class.Meta.fields:   # form의 모든 field에 대하여
            if form.has_error(f):               # validation error가 있는지 확인한 후 있으면
                for err in form.errors[f]:      # 그 error에 관한 messages를 포함하여 render 한다.
                    context = {'message': err, 'form':form}
                    return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        # non-field validation error 및 기타 error를 처리한다.
        context = {'message': form.errors, 'form':form}
        return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

    def form_valid(self, form):
        # 기본적인 validation을 통과한 이후의 과정이다.
        # 다음 두 경우는 form에서 검증한다 - form_invalid()에 해당함.
        # if User.objects.filter(username=data['username']):
        # if data['email'] == '':

        data = form.cleaned_data

        if User.objects.filter(email=data['email']):
            context = {'message':'이미 사용중인 이메일입니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        if data['password1'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        # login(self.request, user)
        return HttpResponseRedirect(self.success_url)