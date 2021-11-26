from django.db import models

# Create your models here.

class Shopping_cart(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.CharField(max_length=100)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
    