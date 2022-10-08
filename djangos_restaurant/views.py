from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Home')
    return render(request, 'index.html')

def menu(request):
    #return HttpResponse('Menu')
    return render(request, 'menu.html')

def book_table(request):
    #return HttpResponse('Book a table')
    return render(request, 'book_table.html')

def my_bookings(request):
    #return HttpResponse('My Bookings')
    return render(request, 'my_bookings.html')

