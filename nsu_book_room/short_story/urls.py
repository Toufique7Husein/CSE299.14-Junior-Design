from django.urls import path
from . import views

urlpatterns = [
   path('shortstory', views.short_story, name='shortstory'),
   path('shortstory/<str:pk>/', views.readShortStory, name='readShortStory')
]
