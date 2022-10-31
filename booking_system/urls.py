from . import views
from django.urls import path

# Urls

urlpatterns = [
    path('menu/', views.DishList.as_view(), name='menu'),
    path('book_table/', views.book_table, name='book'),
    path('my_bookings/', views.booking_list, name='bookings'),
    path('edit/<reservation_id>', views.edit_booking, name='edit'),
    path('delete/<reservation_id>', views.delete_booking, name='delete'),
]
