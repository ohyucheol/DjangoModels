from django.urls import path
from . import views
from .views import CreateView

app_name = 'D01'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateView.as_view())
    # path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    # path('signout/', views.signout, name='signout'),
    # path('change-email', views.change_email, name='change-email'),
    # path('change-password', views.change_password, name='change-password')
]