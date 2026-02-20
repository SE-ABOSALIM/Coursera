from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)