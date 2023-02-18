from django.db import models
from django.conf import settings


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    tier = models.CharField(max_length=20)


