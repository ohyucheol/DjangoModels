from django.urls import path
from .views import About, UserCreateView

app_name = 'A01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('create/', UserCreateView.as_view(), name='create'),
]