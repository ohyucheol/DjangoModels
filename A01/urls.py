from django.urls import path
from .views import About

app_name = 'A01'

urlpatterns = [
    path('', About.as_view(), name='about'),
]