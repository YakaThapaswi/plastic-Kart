from django.db import models
from django.contrib.auth.models import auth,User
from django.contrib import messages
from home.models import Product
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="carts")
    ispaid=models.BooleanField(default="False")
    def __User__(self):
        return self.user
class Cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    def __Cart__(self):
        return self.cart
    
class Whis(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="whis")
    def __User__(self):
        return self.user
class Whisitem(models.Model):
    whis=models.ForeignKey(Whis,on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    def __Cart__(self):
        return self.cart