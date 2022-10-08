from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def menu(request):
    return HttpResponse('Menu')

def book_table(request):
    return HttpResponse('Book a table')

def my_bookings(request):
    return HttpResponse('My Bookings')

    