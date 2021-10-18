from django.db import models
from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=28, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.name


class CommodityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(blank=True)

class Commodity(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    # 这里不是很确定, 我的想法是卖家和商品是一对多的关系，所以设了一个外键
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.ForeignKey(CommodityType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='CommodityPhotos', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    category = models.CharField(max_length=64, blank=True)
    numofstock = models.IntegerField(default=0)
    onsale = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Commodities"
        ordering = ('-addtime',)

    def __unicode__(self):
        return self.name


