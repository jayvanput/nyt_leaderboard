from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Entry(models.Model):

    username = models.TextField()
    hours = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(99)])
    minutes = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(59)])
    seconds = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(59)])
