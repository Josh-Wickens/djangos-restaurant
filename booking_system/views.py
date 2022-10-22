from django.shortcuts import render
from django.views import generic
from .models import FoodMenu, Reservation
from .forms import ReserveTableForm

# Create your views here.


class DishList(generic.ListView):
    model = FoodMenu
    queryset = FoodMenu.objects.all()
    template_name = 'menu.html'


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
    

def book_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.method)

        if reserve_form.is_valid():
            reserve_form.save()
    
    context = {'form' : reserve_form}

    return render(request, 'book_table.html', context)