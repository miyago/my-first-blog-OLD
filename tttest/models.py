from django.db import models

# Create your models here.

class Catalog(models.Model):
    catalog_name1 = models.CharField(max_length=30)
    catalog_name2 = models.CharField(max_length=30)
    catalog_name3 = models.CharField(max_length=30)