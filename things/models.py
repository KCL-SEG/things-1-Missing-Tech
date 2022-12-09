from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.TextField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(unique=False, min_value=0, max_value=100)