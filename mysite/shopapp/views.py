from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def shop_index(request: HttpRequest):

    return render(request, "shopapp/shop-index.html")
