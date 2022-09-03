from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        data = form.cleaned_data

        if data['password'] != data['password2']:
            context = {'message':'비밀번호가 일치하지 않습니다', 'form':form}
            return render(self.request, 'DjangoApps/templates/A01/user-form.html', context)


        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return HttpResponseRedirect(self.success_url)

        #실패한 경우(username 중복, 비밀번호 불일치 등)
        #return redirect()