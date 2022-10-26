from django.shortcuts import render
from django.views import generic
from .models import FoodMenu, Reservation
from .forms import ReserveTableForm
from datetime import timedelta
from django.contrib import messages

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
    


# def check_availablity(requested_date, requested_time):
#     no_tables_booked = len(Reservation.objects.filter(
#         check_in=requested_time,
#         date=requested_date, status="confirmed"))
    
#     return no_tables_booked
    
    # if no_tables_booked >= 10:
    #     print("too many tables")
    # else:
    #     print(no_tables_booked)



def book_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            booking = reserve_form.save(commit=False)
            # check_availablity(booking.date, booking.check_in)
            no_tables_booked = len(Reservation.objects.filter(
                check_in=booking.check_in,
                date=booking.date, status="confirmed"))

            if no_tables_booked >= 10:
                print(no_tables_booked)
            else:
                booking.user = request.user
                booking.save()
                return render(request, 'my_bookings.html')      
            
    context = {'form': reserve_form}

    return render(request, 'book_table.html', context)






    # calc_checkout = booking.check_in + timedelta(minutes=90)
            # booking.check_out = calc_checkout