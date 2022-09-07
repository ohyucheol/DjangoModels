from django.urls import path
from .views import About, CheckBusinessRegistrationNumberView, CheckBusinessInformationView, \
                    LoginUserView, LogoutUserView, \
                    CreateUserView, UpdateUsernameView, UpdateEmailView, UpdatePasswordView, \
                    MyPageView

app_name = 'B01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('check-business-registration-number/', CheckBusinessRegistrationNumberView.as_view(), name='check-business-registration-number'),
    path('check-business-information/', CheckBusinessInformationView.as_view(), name='check-business-information'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/<int:pk>/username/', UpdateUsernameView.as_view(), name='update-username'),
    path('update/<int:pk>/email/', UpdateEmailView.as_view(), name='update-email'),
    path('update/<int:pk>/password/', UpdatePasswordView.as_view(), name='update-password'),
]