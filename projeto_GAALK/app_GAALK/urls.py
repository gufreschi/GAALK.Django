from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.register_user, name='cadastro'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('alterar-nome/', views.new_username, name='new-username'),
    path('alterar-email/', views.new_email, name='new-email'),
    path('excluir-perfil/', views.delete_profile, name='delete-profile'),
    path('sobre/', views.sobre, name='sobre'),
    # path('descobrir/', views.descobrir, name='descobrir'),
    # path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('error/', views.error, name='error'),
    path('search/', views.search, name='search'),
]