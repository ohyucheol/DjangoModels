from django.urls import path
from .views import About, CreateUserView, UpdateUsernameView, UpdateEmailView, UpdatePasswordView

app_name = 'A01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/<int:pk>/username/', UpdateUsernameView.as_view(), name='update-username'),
    path('update/<int:pk>/email/', UpdateEmailView.as_view(), name='update-email'),
    path('update/<int:pk>/password/', UpdatePasswordView.as_view(), name='update-password'),
]