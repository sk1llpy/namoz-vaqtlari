from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=255)
    notification = models.BooleanField(default=True, null=True, blank=True)
    tasbih_counter = models.IntegerField(null=True, blank=True, default=0)
    tasbih_mode = models.IntegerField(null=True, blank=True, default=33)
    region = models.CharField(null=True, blank=True, default="Toshkent", max_length=255)

