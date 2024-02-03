from django.db import models
import datetime
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255,default='')
    link = models.CharField(max_length=2,default='')
    city = models.CharField(max_length=255,default='')
    update = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title


class Last_update(models.Model):
    city = models.CharField(max_length=255,default='')
    update = models.DateTimeField(default=datetime.datetime.today())

    def __str__(self):
        return self.city
