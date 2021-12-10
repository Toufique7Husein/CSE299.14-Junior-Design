from django.urls import path

from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('signup', views.signup, name='signup')
]
