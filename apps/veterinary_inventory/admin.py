from django.contrib import admin
from .models import Category, Product, Stock, Supplier, Transaction

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Transaction)
