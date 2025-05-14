# core/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # Importando auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('agendar/', views.agendar, name='agendar'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),  # Nova URL
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]