from django.db import models

# Create your models here.
class CaptureCO2(models.Model):
    date = models.DateField(auto_now=True)
    ppm = models.IntegerField(blank=False, null=False, default=0)