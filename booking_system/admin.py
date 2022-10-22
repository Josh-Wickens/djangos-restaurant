from django.contrib import admin
from .models import FoodMenu, Tables, Reservation


# Register your models here.

admin.site.register(FoodMenu)
admin.site.register(Tables)
admin.site.register(Reservation)
