"""
URL configuration for MyFintessPal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('food/', include("food.urls")),
    path('help/', include("help.urls")),
    path('account/', include("settings.urls")),
    path('authentication/', include("authentication.urls")),
    path('user_profile/', include("user_profile.urls")),
    path('weight/', include('weight.urls')),
    path('exercises/', include('exercises.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
