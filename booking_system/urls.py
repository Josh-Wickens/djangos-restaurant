from . import views
from django.urls import path


urlpatterns = [
    path('menu/', views.DishList.as_view(), name='menu'),
    path('book_table/', views.book_table, name='book'),
]
