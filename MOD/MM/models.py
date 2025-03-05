from django.db import models

# Create your models here.
class A(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    play = models.CharField(max_length=100)
