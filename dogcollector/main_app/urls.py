from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('dogs/', views.index, name='index'),
    path('dogs/<int:dog_id>/', views.detail, name='detail'),
    path('dogs/create/', views.create_dog, name='create_dog'),
    path('dogs/<int:dog_id>/update/', views.update_dog, name='update_dog'),
    path('dogs/<int:dog_id>/delete/', views.delete_dog, name='delete_dog'),

    path('owners/', views.owner_index, name='owner_index'),
    path('owners/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owners/create/', views.create_owner, name='create_owner'),
    path('owners/<int:owner_id>/update/', views.update_owner, name='update_owner'),
    path('owners/<int:owner_id>/delete/', views.delete_owner, name='delete_owner'),
    path('toys/', views.toy_index, name='toy_index'),
    path('toys/<int:toy_id>/', views.toy_detail, name='toy_detail'),
    path('toys/create/', views.create_toy, name='create_toy'),
    path('toys/<int:toy_id>/update/', views.update_toy, name='update_toy'),
    path('toys/<int:toy_id>/delete/', views.delete_toy, name='delete_toy'),
]
