from django.db import models

# Create your models here.
class Cyber(models.Model):
    name = models.CharField(max_length = 22)
    surname = models.CharField(max_length = 22)
    coments = models.TextField()