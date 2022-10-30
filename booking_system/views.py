from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import FoodMenu, Reservation, Table
from .forms import ReserveTableForm
import datetime
from datetime import date
from datetime import timedelta
from django.contrib import messages


# Create your views here.


class DishList(generic.ListView):
    model = FoodMenu
    queryset = FoodMenu.objects.all()
    template_name = 'menu.html'


def booking_list(request):
    reservations = list(Reservation.objects.filter(user=request.user, status="confirmed"))
    today = date.today()

    for index, reservation in enumerate(reservations):
        if reservation.date < today:
            reservation.status = 'expired'
            reservation.save()
            del reservations[index]
    context = {
        'bookings': reservations
    }

    return render(request, "my_bookings.html", context)


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
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            booking = reserve_form.save(commit=False)
            no_tables_booked = len(Reservation.objects.filter(
                check_in=booking.check_in,
                date=booking.date, status="confirmed"))

            if no_tables_booked >= 7:
                messages.error(request, "Sorry there are no tables available at this time.")

            else:
                booking.user = request.user
                booking.status = "confirmed"
                booking.save()
                messages.success(request, "Your booking for has been confirmed.")
                return redirect('bookings')

    context = {'form': reserve_form}

    return render(request, 'book_table.html', context)


def edit_booking(request, reservation_id):
    booking = get_object_or_404(Reservation, reservation_id=reservation_id)
    today = date.today()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST, instance=booking)

        if reserve_form.is_valid():
            booking = reserve_form.save(commit=False)
            no_tables_booked = len(Reservation.objects.filter(
                check_in=booking.check_in,
                date=booking.date, status="confirmed"))

            if no_tables_booked >= 10:
                messages.error(request, "Sorry there are no tables available at this time.")

            else:
                booking.user = request.user
                booking.status = "confirmed"
                booking.save()
                messages.success(request, "Your booking has been confirmed.")
                return redirect('bookings')
    reserve_form = ReserveTableForm(instance=booking)
    context = {'form': reserve_form}
    return render(request, 'edit_booking.html', context)


def delete_booking(request, reservation_id):
    booking = get_object_or_404(Reservation, reservation_id=reservation_id)
    booking.delete()
    return redirect('bookings')
