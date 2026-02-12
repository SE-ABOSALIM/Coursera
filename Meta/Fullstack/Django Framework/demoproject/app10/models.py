from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.BinaryField(max_length=10)
