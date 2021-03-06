from django.urls import path

from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('signup', views.signup, name='signup'),
    path('user_profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('edit_profile/<str:pk>/', views.edit_profile, name='edit_profile')
]
