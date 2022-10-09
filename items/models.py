from tabnanny import verbose
from turtle import onclick
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    iName = models.CharField(max_length=200)
    def __str__(self):
        return self.iName


class Item(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, verbose_name='Item Name')
    price = models.IntegerField(verbose_name='Item Price')
    img = models.FileField(upload_to='index/', null=True, blank=True, verbose_name='Item Image')

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
#     image = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
#     price = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    