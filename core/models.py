from django.db import models

class Vegetables(models.Model):
    name = models.CharField(max_length=50,default='N/A')
    price = models.FloatField(default=9.99)
    quantity = models.FloatField(default=1)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='item_images',default='item_images/dflt.png')

class User(models.Model):
    username = models.CharField(max_length=30,unique=True,null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(default='2000-12-31',blank=True,null=True)