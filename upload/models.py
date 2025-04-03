from django.db import models
from django.db.models import Manager


class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(unique=True)
    date = models.DateField()

    objects = Manager()

    def __str__(self):
        return self.title
