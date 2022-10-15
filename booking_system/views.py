from django.shortcuts import render
from django.views import generic
from .models import FoodMenu

# Create your views here.


# class DishList(generic.ListView):
#     model = FoodMenu
#     queryset = FoodMenu.objects
#     template_name = 'menu.html'


def FoodMenu(request):
    dishes = FoodMenu.objects.all().order_by('food_type')
    context = {
        'name': name,
        'description': description,
        'food_type': food_type,
        'price': price,
        'vegetarian': vegetarian,
        'vegan': vegan,
    }
    