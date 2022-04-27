from django.shortcuts import render
from .models import Product, PythonClubType, Review

# Create your views here.
def index(request):
    return render(request,'PythonClub/index.html')

def products(request):
    product_list = Product.objects.all()
    return render (request, 'PythonClub/products.html', 
    {'product_list': product_list})


