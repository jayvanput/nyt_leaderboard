from django.db import models

# Create your models here.


class Entry(models.Model):

    username = models.TextField()
    solve_time = models.IntegerField(default=0)
