from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    # return HttpResponse('Home')
    return render(request, 'index.html')
