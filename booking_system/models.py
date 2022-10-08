from django.db import models

# Create your models here.

class Tables(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.IntegerField(max_length=6)
    window = models.BooleanField()
