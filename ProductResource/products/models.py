from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)#The name of the product
  description = models.CharField(max_length=100)#The product description
  price = models.DecimalField(max_digits=10, decimal_places=2)#The price of the product
  
def __str__(self):
        return self.name 