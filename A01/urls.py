from django.urls import path
from .views import About, LoginUserView, LogoutUserView, \
                    CreateUserView, UpdateUsernameView, UpdateEmailView, UpdatePasswordView, \
                    UpdateBannedKeywordView, PersonalUserView

app_name = 'A01'

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('<str:username>/', PersonalUserView.as_view(), name='personal'),
    path('update-banned-keyword/', UpdateBannedKeywordView.as_view(), name='update-banned-keyword'),
    path('update/<int:pk>/username/', UpdateUsernameView.as_view(), name='update-username'),
    path('update/<int:pk>/email/', UpdateEmailView.as_view(), name='update-email'),
    path('update/<int:pk>/password/', UpdatePasswordView.as_view(), name='update-password'),
]