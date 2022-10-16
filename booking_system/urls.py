from . import views
from django.urls import path


urlpatterns = [
    path('', views.DishList.as_view(), name='menu')
]