from django.shortcuts import render
from django.views import generic
from .models import FoodMenu, Reservation
from .forms import ReserveTableForm
from datetime import timedelta

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
    

# class check_reservation(Reservation):
#     for booking in Reservation:
#         for date in booking:
            
#             def remove_times(date):
#                 booking.date.time.remove
    






def book_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            booking = reserve_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'my_bookings.html')      
            
    context = {'form': reserve_form}

    return render(request, 'book_table.html', context)



    # calc_checkout = booking.check_in + timedelta(minutes=90)
            # booking.check_out = calc_checkout