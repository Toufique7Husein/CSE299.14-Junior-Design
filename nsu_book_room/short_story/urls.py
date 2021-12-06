from django.urls import path
from . import views

urlpatterns = [
   path('shortstory', views.short_story, name='shortstory'),
   path('shortstory/<str:pk>/', views.readShortStory, name='readShortStory'),
   path('shortstory_from', views.creatShortStory, name='shortstory_from'),
   path('editshortstory/<str:pk>/', views.updateShortStory, name='editshortstory')
]
