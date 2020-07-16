from django.db import models

# Create your models here.
#活动表
class Activity(models.Model):
    cname = models.CharField(max_length=200)
    ctime = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)
    urlLink = models.CharField(max_length=150)

#用户表
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
