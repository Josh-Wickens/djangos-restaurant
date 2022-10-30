from django.contrib import admin
from .models import FoodMenu, Table, Reservation


# Register your models here.

class Filter(admin.ModelAdmin):
    list_display = ("date", "check_in", "status", "table", "reservation_id")
    list_filter = ("date", "check_in", "status", "table", "reservation_id")
    search_fields = ("date", "check_in", "reservation_id", "user",)


admin.site.register(FoodMenu)
admin.site.register(Table)
admin.site.register(Reservation, Filter)
