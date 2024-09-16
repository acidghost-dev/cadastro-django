from django.urls import path
from app_cadastro_usuarios import views
urlpatterns = [
    path('', views.index,name='index'),
    path('usuarios/', views.usuarios,name='usuarios'),
]
