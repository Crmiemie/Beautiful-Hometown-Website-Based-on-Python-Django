from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2)
    city = models.CharField(max_length=10, default='北京')
    # image = models.ImageField(upload_to='item_images', blank=True, null=True)
    belongs_to = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Location_Pic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    description = models.TextField(max_length=4096, default='暂无')
    def __str__(self):
        return self.name


class City_Feature(models.Model):
    name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    description = models.TextField(max_length=4096, default='暂无')
    def __str__(self):
        return self.name


class Moment(models.Model):
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=4096,default='')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    belongs_to = models.ForeignKey(User, related_name='moments', on_delete=models.CASCADE)
    def __str__(self):
        return self.title