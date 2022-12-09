from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    quantity = models.IntegerField()