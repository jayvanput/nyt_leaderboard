from django.db import models

# Create your models here.


class Entry(models.Model):

    username = models.CharField(max_length=20)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
