from django.urls import path 
from django.contrib.auth import views as auth_views
from weight import views

urlpatterns = [
    path('update-weight/', views.update_weight, name='update_weight'),
    path('weight-tracker/', views.weight_tracker, name='weight_tracker'),
]
