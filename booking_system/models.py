from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
FOOD_TYPES = (
          ('Starter', 'Starter'),
          ('Mains', 'Mains'),
          ('Dessert', 'Dessert'),
)

TIME_CHOICES = (
    ("18:00 - 19:30", "18:00 - 19:30"),
    ("18:30 - 20:00", "18:30 - 20:00"),
    ("19:00 - 20:30", "19:00 - 20:30"),
    ("19:30 - 21:00", "19:30 - 21:00"),
    ("20:00 - 21:30", "20:00 - 21:30"),
    ("20:30 - 22:00", "20:30 - 22:00"),
    ("21:00 - 22:30", "21:00 - 22:30"),
    ("21:30 - 23:00", "21:30 - 23:00"),
    ("22:00 - 23:30", "22:00 - 23:30"),
)


class FoodMenu(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=80, blank=False, default="insert description")
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    vegetarian = models.BooleanField(null=False, blank=False, default=False)
    vegan = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f" Table No. - {self.table_number}"


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    guests = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
     )
    date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    time = models.CharField(max_length=20, choices=(TIME_CHOICES))

    def __str__(self):
        return f"Ref No. {self.reservation_id} - {self.name}"
