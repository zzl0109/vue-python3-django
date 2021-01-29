from django.db import models
from django.contrib import admin

# Create your models here.


class Customer(models.Model):
    # 名字
    name = models.CharField(max_length=200)

    # 手机
    phone_number = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    qq = models.CharField(max_length=20, null=True, blank=True)


admin.site.register(Customer)
