from django.db import models
from django.contrib.auth.models import auth,User
class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Wallet")
    amount=models.IntegerField(default=0)
