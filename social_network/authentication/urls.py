
from django.urls import path
from django.conf.urls import url

from rest_auth.registration.views import RegisterView, LoginView, VerifyEmailView
from rest_auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LogoutView

from allauth.account.views import confirm_email, email_verification_sent

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', PasswordChangeView.as_view(), name='password-change'),
    path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
    path('logout/', LogoutView.as_view(), name='logout'),
    url(r'^confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    url(r'^confirm-email/$', VerifyEmailView.as_view(), name='account_confirm_email_with_code'),
    url(r'^confirm-email-sent/$', email_verification_sent, name='account_email_verification_sent'),
    url(r'^reset-password/confirm/(?P<uidb64>.+)/(?P<token>.+)$', PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
]