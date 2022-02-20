from math import prod
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Book, Cupboard

def home(request):
    # products  = Product.objects.all().select_related('content_type')
    # products  = Product.objects.all().select_related('book','cupboard')
    cup = Cupboard.objects.all()
    book = Book.objects.all()
    products = cup.union(book)
    return render(request,'home.html',{'products':products})