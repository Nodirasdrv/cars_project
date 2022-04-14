from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivateUserAccount.as_view(),
         name='activate_account'),
    path('auth/', include('rest_framework.urls')),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
]
