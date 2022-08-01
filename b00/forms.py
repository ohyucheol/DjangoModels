from django import forms

class SigninForm(forms.Form):
    username = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

class SignupForm(forms.Form):
    username = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

class ChangeEmailForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))