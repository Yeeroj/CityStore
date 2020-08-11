from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShopDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    shopname=models.CharField(max_length=200)
    gstno=models.CharField(max_length=40,null=True,default="Not Available")
    address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10,null=True)
    holiday=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    shopowner=models.CharField(max_length=200)

    def __str__(self):
        return self.shopname


class Product(models.Model):
    name=models.CharField(max_length=200)
    # shop=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='images/',null=True)
    price=models.CharField(max_length=20,default="Not Available")
    description=models.CharField(max_length=200,null=True,default="Description:NA")
    shopname=models.CharField(max_length=200,null=True,default="NOT")

    def __str__(self):
        return self.name


