from django.urls import path
from . import views

urlpatterns = [
    path("", views.help, name="help"),
    path("reports/", views.report, name="reports"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("privacy_policy_full/", views.privacy_policy_full, name="privacy_policy_full")
]