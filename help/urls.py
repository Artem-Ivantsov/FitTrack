from django.urls import path
from . import views

urlpatterns = [
    path("", views.help,name="help"),
    path("reports/", views.report,name="reports"),



]