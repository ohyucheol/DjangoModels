from django.urls import path
from . import views

app_name = 'J01'

urlpatterns = [
    path('', views.about, name='about'),
]