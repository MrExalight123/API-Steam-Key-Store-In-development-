from django.urls import path
from allauth.account.views import ConfirmEmailView
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import User_Information_viewset

rouder = DefaultRouter()

rouder.register(r'User_Information', User_Information_viewset)

urlpatterns = [
    # URL для подтверждения почты (пользователь кликает по ссылке из письма)
    path('confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    # Страница после успешного подтверждения почты
    path('email-confirmed/', TemplateView.as_view(template_name='accaunt/email_confirmed.html'), name='email_confirmed'),
]

urlpatterns += rouder.urls