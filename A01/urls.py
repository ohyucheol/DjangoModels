from django.urls import path
from .views import About, CreateUserView

app_name = 'A01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('create/', CreateUserView.as_view(), name='create'),
]