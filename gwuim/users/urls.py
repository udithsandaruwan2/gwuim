from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]