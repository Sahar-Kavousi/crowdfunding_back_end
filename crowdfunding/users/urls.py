from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('user/', views.CustomUserDetail.as_view(), name='user-detail'),
    path('user/<int:pk>/', views.CustomUserDetail.as_view(), name='specific-user-detail'),
    ]

