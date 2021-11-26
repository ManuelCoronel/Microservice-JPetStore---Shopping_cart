from enum import auto
from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(blank='',default="",upload_to="photos/")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.description



    


