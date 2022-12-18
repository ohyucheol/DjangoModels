from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.

from .forms import CheckBusinessRegistrationNumberForm, CheckBusinessInformationForm, \
                    CreateUserForm, UpdateUsernameForm, UpdateEmailForm, \
                    UpdatePasswordForm, LoginUserForm

# Create your views here.

class About(TemplateView):
    template_name = "DjangoModels/templates/B01/about.html"

class CheckBusinessRegistrationNumberView(FormView):
    form_class = CheckBusinessRegistrationNumberForm
    template_name = 'DjangoModels/templates/B01/check-business-registration-number.html'
    success_url = '/B01/check-business-information'

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

        # CheckBusinessInformationView에서 사업자상태 및 사업자정보를 조회할 수 있도록
        # 사업자등록번호를 쿼리스트링으로 넘겨준다.
        self.success_url = self.success_url + '?brn=' + str(data['business_registration_number'])

        return super().form_valid(form)

class CheckBusinessInformationView(FormView):
    form_class = CheckBusinessInformationForm
    template_name = 'DjangoModels/templates/B01/check-business-information.html'
    success_url = '/B01/create'

    def get_initial(self):
        
        if 'brn' in self.request.GET:
            self.initial['business_registration_number'] = int(self.request.GET['brn'])

        # 사업자상태 조회 구현(data.go.kr API 승인 필요)
        # 사업자정보 조회 구현(nicebizdata.com API 승인 필요)
        # 다음의 값은 API를 이용하여 필요한 값을 받아온 것으로 간주한다.

        self.initial['b_stt'] = 'b_stt 값'
        self.initial['tax_type'] = 'tax_type 값'
        self.initial['end_dt'] = 'end_dt 값'
        self.initial['utcc_yn'] = 'utcc_yn 값'
        self.initial['tax_type_change_dt'] = 'tax_type_change_dt 값'
        self.initial['invoice_apply_dt'] = 'invoice_apply_dt 값'

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
        data = form.cleaned_data

        # 필요시 '인격권 등'의 모델에 입력받은 사업자상태 및 정보를 저장한다.

        return super().form_valid(form)

class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'DjangoModels/templates/B01/create-user.html'
    success_url = '/B01/'

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

        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = template_name = 'DjangoModels/templates/B01/login-user.html'

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
    template_name = 'DjangoModels/templates/B01/login-user.html'

class MyPageView(TemplateView):
    template_name = "DjangoModels/templates/B01/mypage.html"

    def get_context_data(self, **kwargs):
        page_owner = User.objects.get(username=kwargs['username'])
        self.extra_context = {'page_owner' : page_owner}
        kwargs.update(self.extra_context)
        
        return kwargs

class UpdateUsernameView(UpdateView):
    model = User
    form_class = UpdateUsernameForm
    initial = {'username' : ''}
    template_name = "DjangoModels/templates/B01/update-username.html"
    success_url = '/B01/'

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
    template_name = "DjangoModels/templates/B01/update-email.html"
    success_url = '/B01/'

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
    template_name = 'DjangoModels/templates/B01/update-password.html'
    success_url = '/B01/'

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
