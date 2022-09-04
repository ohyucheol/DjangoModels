from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserCreateForm
# Create your views here.

class About(TemplateView):
    template_name = "DjangoApps/templates/A01/about.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'DjangoApps/templates/A01/user-form.html'
    success_url = '/A01/'

    def form_invalid(self, form):
        #번역필요
        err = dict(form.errors)
        messages = ''
        # err = form.errors.as_text()
        # context = {'message': form.errors.as_text(), 'form':form}
        # print(err)
        for e in err.values():
            print(e)
            messages = messages + e
        context = {'message': form.errors, 'form':form}
        return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        # messages = dict(form.errors)

        # print(messages)
        # for key in messages:
        #     print(key)

        # if form.has_error('username'):
        #     context = {'message': '사용할 수 없는 아이디입니다', 'form':form}
        #     return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        # if form.has_error('email'):
        #     context = {'message': '사용할 수 없는 이메일입니다', 'form':form}
        #     return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        # if form.has_error('password') or form.has_error('password2'):
        #     context = {'message': '사용할 수 없는 비밀번호입니다', 'form':form}
        #     return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        # #그밖의 에러
        # context = {'message': form.errors, 'form':form}
        # return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        data = form.cleaned_data

        if User.objects.filter(username=data['username']):
            context = {'message':'이미 사용중인 아이디입니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        if data['email'] == '': 
            context = {'message':'이메일을 입력하세요', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        if User.objects.filter(email=data['email']):
            context = {'message':'이미 사용중인 이메일입니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        if data['password'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)

        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        # login(self.request, user)
        return HttpResponseRedirect(self.success_url)

        #실패한 경우(username 중복, 비밀번호 불일치 등)
        #return redirect()