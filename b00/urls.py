from django.urls import path
from . import views

app_name = 'a00'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('change-email', views.change_email, name='change-email'),
    path('change-password', views.change_password, name='change-password')
]