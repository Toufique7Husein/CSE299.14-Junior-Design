from django.urls import path
from . import views

urlpatterns = [
   path('discussion', views.discussion_home, name='discussion_home'),
  # path('shortstory/<str:pk>/', views.readShortStory, name='readShortStory'),
]