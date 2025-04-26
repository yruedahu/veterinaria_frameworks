from django.shortcuts import render, get_object_or_404
from .models import Product

def inventory_home(request):
    return render(request, 'veterinary_inventory/inventory_home.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'category': product.category.name,
        'supplier': product.supplier.name if product.supplier else "Sin proveedor",
        'price': product.price,
        'description': product.description,
        'stock': product.stock.quantity if hasattr(product, 'stock') else 0
    }
    return render(request, 'veterinary_inventory/product_detail.html', context)