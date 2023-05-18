from django.db import models
class Orders(models.Model):
    orderId=models.IntegerField()
    status=models.CharField(max_length=30)
    date=models.DateField()
    image=models.URLField()
    def __str__(self):
        return self.orderId
