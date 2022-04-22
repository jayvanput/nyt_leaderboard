from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from datetime import date
# Create your models here.


class Entry(models.Model):

    username = models.TextField()
    hours = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(99)])
    minutes = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(59)])
    seconds = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(59)])
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.created}: {self.username}"