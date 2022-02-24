from django.db import models

# Create your models here.


class Entry(models.Model):

    username = models.TextField()
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    solve_time = models.IntegerField()
