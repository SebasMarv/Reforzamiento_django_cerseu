from django.db import models

# Create your models here.
class Catalog(models.Model):
    garment = models.CharField(max_length=100,default='')
    classification = models.CharField(max_length=40, default='')
    price = models.IntegerField()