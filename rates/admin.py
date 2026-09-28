from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Material, PriceQuote

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(PriceQuote)