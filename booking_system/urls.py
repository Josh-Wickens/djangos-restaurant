from . import views
from django.urls import path


urlpatterns = [
    path('menu/', views.DishList.as_view(), name='menu'),
    path('', views.book_table, name='book'),
]
