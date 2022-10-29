from django.db import models
import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

FOOD_TYPES = (
          ('Starter', 'Starter'),
          ('Mains', 'Mains'),
          ('Dessert', 'Dessert'),
)

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('expired', 'expired'),
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
    phoneNumber = PhoneNumberField(null=False, blank=False, default="+44")
    guests = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    date = models.DateField()
    check_in = models.TimeField(default=datetime.time(18, 00))
    pending = "pending"
    confirmed = "confirmed"
    expired = "expired"
    status_choices = ((pending, "pending"), (confirmed, "confirmed"))
    status = models.CharField(max_length=20,  choices=STATUS_CHOICES, default=pending)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f"Ref No. {self.reservation_id} - {self.name}"

    class Meta:
        ordering = ['date']
