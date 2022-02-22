from django.shortcuts import render
from .models import Product, Book, Cupboard

def home(request):
    # products  = Product.objects.all().select_related('content_type')
    # products  = Product.objects.all().select_related('book','cupboard')
    # cup = Cupboard.objects.all()
    # book = Book.objects.all()
    # products = cup.union(book)
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})
