from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (
    ActivateUserEmailView,
    CustomResetPasswordConfirmView,
    CustomResetPasswordView,
    LoginView,
    RegisterView,
)


urlpatterns = [
    # path('oauth/', include('social_django.urls', namespace='social')),
    # path('oauth/login-success/', google_login, name='google_login'),
    # path('google-account-info/', google_account_info, name='google_account_info'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'reset-password/',
        CustomResetPasswordView.as_view({'post': 'reset_password'}),
        name='reset-password',
    ),
    path(
        'reset-password-confirm/',
        CustomResetPasswordConfirmView.as_view({'post': 'reset_password_confirm'}),
        name='reset_password_confirm',
    ),
    path('activate/<str:uid>/<str:token>/', ActivateUserEmailView.as_view(), name='activate email'),
]
