from django.db import models
from django.conf import settings

class Exercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    muscle_group = models.CharField(max_length=50, null=True)
    equipment = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.name
    
class Useful_Materials(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to="meterials_video", blank=True, null=True)
    image = models.FileField(upload_to="materials_photo", blank=True, null=True)
    app_link_name =models.CharField(max_length=100, blank=True, null=True)
    app_link = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title