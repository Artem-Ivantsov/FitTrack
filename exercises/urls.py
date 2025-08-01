from django.urls import path
from . import views

urlpatterns = [
    path('', views.sport_exercises_view, name='sport_exercises_view'),
    path('my_exercises/', views.my_exercises_view, name='my_exercises'),
    path('videos/', views.video_gallery, name='video_gallery'),
]
