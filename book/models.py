from django.db import models
from django.contrib.auth.models import auth,User
from home.models import Product

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="address")
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    code=models.IntegerField()
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=100)
    area=models.CharField(max_length=20)
    flat=models.CharField(max_length=5)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="order")
    addressid=models.ForeignKey(Address,on_delete=models.CASCADE,related_name="order")
    status=models.CharField(default="placing",max_length=20)
    date=models.DateField()
    itemid=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order")

class Sell(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sell")
    addressid=models.ForeignKey(Address,on_delete=models.CASCADE,related_name="sell")
    status=models.CharField(default="placing",max_length=20)
    date=models.DateField()

