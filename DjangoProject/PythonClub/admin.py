from django.contrib import admin
from .models import PythonClubType, Product, Review

# Register your models here.

admin.site.register(PythonClubType)
admin.site.register(Product)
admin.site.register(Review)