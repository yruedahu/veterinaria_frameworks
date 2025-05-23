from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category, Supplier, Stock, Transaction
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
import pandas as pd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io

def inventory_home(request):
    return render(request, 'veterinary_inventory/inventory_home.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    next_product = Product.objects.filter(id__gt=product_id).order_by('id').first()
    prev_product = Product.objects.filter(id__lt=product_id).order_by('-id').first()
    context = {
        'product': product,
        'next_product': next_product,
        'prev_product': prev_product,
        'category': product.category.name,
        'supplier': product.supplier.name if product.supplier else "Sin proveedor",
        'price': product.price,
        'description': product.description,
        'stock': product.stock.quantity if hasattr(product, 'stock') else 0
    }
    return render(request, 'veterinary_inventory/product/product_detail.html', context)

def product_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    context = {
        'products': products,
    }
    return render(request, 'veterinary_inventory/product/product_list.html', context)

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        category_id = request.POST['category']
        supplier_id = request.POST.get('supplier')
        description = request.POST.get('description', '')
        price = request.POST['price']
        category = get_object_or_404(Category, pk=category_id)
        supplier = Supplier.objects.get(pk=supplier_id) if supplier_id else None
        product = Product.objects.create(
            name=name,
            category=category,
            supplier=supplier,
            description=description,
            price=price
        )
        Stock.objects.create(product=product)
        messages.success(request, 'Producto creado exitosamente.')
        return redirect('product_list')
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'veterinary_inventory/product/product_form.html', {'categories': categories, 'suppliers': suppliers})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.category_id = request.POST['category']
        product.supplier_id = request.POST.get('supplier')
        product.description = request.POST.get('description', '')
        product.price = request.POST['price']
        product.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('product_list')
    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'veterinary_inventory/product/product_form.html', {'product': product, 'categories': categories, 'suppliers': suppliers})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('product_list')
    return render(request, 'veterinary_inventory/product/product_confirm_delete.html', {'product': product})

def product_stock_alerts(request):
    low_stock_products = Stock.objects.filter(quantity__lte=F('min_stock'))
    return render(request, 'veterinary_inventory/product/stock_alerts.html', {'low_stock_products': low_stock_products})

# CRUD de Proveedores

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'veterinary_inventory/supplier/supplier_list.html', {'suppliers': suppliers})

def supplier_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        Supplier.objects.create(name=name, contact=contact, email=email, phone=phone, address=address)
        messages.success(request, 'Proveedor creado exitosamente.')
        return redirect('supplier_list')
    return render(request, 'veterinary_inventory/supplier/supplier_form.html')

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.name = request.POST['name']
        supplier.contact = request.POST['contact']
        supplier.email = request.POST['email']
        supplier.phone = request.POST['phone']
        supplier.address = request.POST['address']
        supplier.save()
        messages.success(request, 'Proveedor actualizado exitosamente.')
        return redirect('supplier_list')
    return render(request, 'veterinary_inventory/supplier/supplier_form.html', {'supplier': supplier})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Proveedor eliminado exitosamente.')
        return redirect('supplier_list')
    return render(request, 'veterinary_inventory/supplier/supplier_confirm_delete.html', {'supplier': supplier})

# CRUD de Categorías

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'veterinary_inventory/category/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')
        Category.objects.create(name=name, description=description)
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('category_list')
    return render(request, 'veterinary_inventory/category/category_form.html')

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.description = request.POST.get('description', '')
        category.save()
        messages.success(request, 'Categoría actualizada exitosamente.')
        return redirect('category_list')
    return render(request, 'veterinary_inventory/category/category_form.html', {'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('category_list')
    return render(request, 'veterinary_inventory/category/category_confirm_delete.html', {'category': category})

def movement_list(request):
    movements = Transaction.objects.select_related('product').order_by('-date')
    return render(request, 'veterinary_inventory/movement/movement_list.html', {'movements': movements})

def movement_create(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        transaction_type = request.POST['transaction_type']
        quantity = int(request.POST['quantity'])
        note = request.POST.get('note', '')
        product = get_object_or_404(Product, pk=product_id)
        # Actualiza stock
        stock = product.stock
        if transaction_type == 'IN':
            stock.quantity += quantity
        elif transaction_type == 'OUT':
            stock.quantity = max(0, stock.quantity - quantity)
        stock.save()
        Transaction.objects.create(
            product=product,
            transaction_type=transaction_type,
            quantity=quantity,
            note=note,
            date=timezone.now()
        )
        messages.success(request, 'Movimiento registrado exitosamente.')
        return redirect('movement_list')
    products = Product.objects.all()
    return render(request, 'veterinary_inventory/movement/movement_form.html', {'products': products})

def export_products(request, filetype):
    products = Product.objects.select_related('category', 'supplier').all()
    data = []
    for p in products:
        data.append({
            'ID': p.id,
            'Nombre': p.name,
            'Categoría': p.category.name if p.category else '',
            'Proveedor': p.supplier.name if p.supplier else '',
            'Descripción': p.description,
            'Precio': float(p.price),
            'Stock': p.stock.quantity if hasattr(p, 'stock') else 0,
            'Stock mínimo': p.stock.min_stock if hasattr(p, 'stock') else 0,
        })
    df = pd.DataFrame(data)
    if filetype == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=productos.csv'
        df.to_csv(path_or_buf=response, index=False, encoding='utf-8-sig')
    else:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
        with io.BytesIO() as b:
            df.to_excel(b, index=False)
            response.write(b.getvalue())
    return response

@csrf_exempt
def import_products(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        ext = file.name.split('.')[-1].lower()
        if ext == 'csv':
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        for _, row in df.iterrows():
            category, _ = Category.objects.get_or_create(name=row.get('Categoría', 'Sin categoría'))
            supplier = None
            if row.get('Proveedor'):
                supplier, _ = Supplier.objects.get_or_create(name=row['Proveedor'], defaults={'contact':'','email':'','phone':'','address':''})
            product, created = Product.objects.get_or_create(
                name=row['Nombre'],
                defaults={
                    'category': category,
                    'supplier': supplier,
                    'description': row.get('Descripción', ''),
                    'price': row.get('Precio', 0),
                }
            )
            if created:
                Stock.objects.create(product=product, quantity=row.get('Stock', 0), min_stock=row.get('Stock mínimo', 5))
        messages.success(request, 'Importación de productos completada.')
        return redirect('product_list')
    return render(request, 'veterinary_inventory/product/import_products.html')


def export_movements(request, filetype):
    movements = Transaction.objects.select_related('product').all()
    data = []
    for m in movements:
        data.append({
            'ID': m.id,
            'Producto': m.product.name,
            'Tipo': m.get_transaction_type_display(),
            'Cantidad': m.quantity,
            'Fecha': m.date.strftime('%Y-%m-%d %H:%M'),
            'Nota': m.note,
        })
    df = pd.DataFrame(data)
    if filetype == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=movimientos.csv'
        df.to_csv(path_or_buf=response, index=False, encoding='utf-8-sig')
    else:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=movimientos.xlsx'
        with io.BytesIO() as b:
            df.to_excel(b, index=False)
            response.write(b.getvalue())
    return response


def export_suppliers(request, filetype):
    suppliers = Supplier.objects.all()
    data = []
    for s in suppliers:
        data.append({
            'ID': s.id,
            'Nombre': s.name,
            'Contacto': s.contact,
            'Email': s.email,
            'Teléfono': s.phone,
            'Dirección': s.address,
        })
    df = pd.DataFrame(data)
    if filetype == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=proveedores.csv'
        df.to_csv(path_or_buf=response, index=False, encoding='utf-8-sig')
    else:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=proveedores.xlsx'
        with io.BytesIO() as b:
            df.to_excel(b, index=False)
            response.write(b.getvalue())
    return response