from django.db import models

# Create your models here.
FOOD_TYPES = (
          ('Starter', 'Starter'),
          ('Mains', 'Mains'),
          ('Dessert', 'Dessert'),
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


class Tables(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return self.table_number
