from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_dishes_view, name='my_dishes'),
    path('sport_recipes/', views.sport_recipes_view, name='sport_recipes_view'),
    path('spec/', views.special_menu, name='special_menu'),
    path('my_selection/', views.my_selection, name='my_selection'),
]