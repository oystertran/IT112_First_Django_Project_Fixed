from django.shortcuts import render, get_object_or_404
from .models import Product, PythonClubType, Review
from django.urls import reverse_lazy
from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request,'PythonClub/index.html')

def products(request):
    product_list = Product.objects.all()
    return render (request, 'PythonClub/products.html', 
    {'product_list': product_list})

def productdetail (request,id):
    product = get_object_or_404(Product, pk = id)
    return render(request,'PythonClub/productdetail.html',
    {'product': product})

def newProduct(request):
    form = ProductForm

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ProductForm
    else:
        form = ProductForm()
    return render(request,'pythonclub/newproduct.html',
    {'form':form})