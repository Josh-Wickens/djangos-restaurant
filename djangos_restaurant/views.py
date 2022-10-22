from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    # return HttpResponse('Home')
    return render(request, 'index.html')


@login_required()
def book_table(request):
    #return HttpResponse('Book a table')
    return render(request, 'book_table.html')

@login_required()
def my_bookings(request):
    #return HttpResponse('My Bookings')
    return render(request, 'my_bookings.html')

