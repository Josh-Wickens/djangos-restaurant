from django.contrib import admin
from .models import FoodMenu, Table, Reservation


# Register your models here.

admin.site.register(FoodMenu)
admin.site.register(Table)
admin.site.register(Reservation)
