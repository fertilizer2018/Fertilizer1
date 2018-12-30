from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.CharField(max_length=300)


class Employe(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
