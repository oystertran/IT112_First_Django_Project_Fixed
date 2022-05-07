from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products/',views.products, name='products'),
    path('productdetail/<int:id>', views.productdetail, 
    name = 'detail'),
    path('newproduct', views.newProduct, name = 'newproduct'),
]