from django.urls import path
from . import views

urlpatterns = [
   path('longstory', views.long_story, name='longstory'),
   path('longstory/<str:pk>/', views.readLongStory, name='readLongStory'),
   path('longstory_from', views.creatLongStory, name='longstory_from'),
   path('editlongstory/<str:pk>/', views.updateLongStory, name='editlongstory')
]
