from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)

class Learner(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    course_id = models.ForeignKey(
        Course,
        on_delete= models.PROTECT,
        default=None,
    )