from django.db import models
class Product(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=30)
    prize=models.IntegerField()
    category=models.CharField(max_length=30)
    image=models.URLField()
    def __str__(self):
        return self.name
class Variant(models.Model):
    category=models.CharField(max_length=30)
    image=models.ImageField(upload_to="home/image")
    def __str__(self):
        return self.category
