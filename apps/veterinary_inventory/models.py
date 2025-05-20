from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre del proveedor")
    contact = models.CharField(max_length=100, verbose_name="Contacto")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    address = models.TextField(verbose_name="Dirección")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del producto")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen del producto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stock")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Cantidad en stock")
    min_stock = models.PositiveIntegerField(default=5, verbose_name="Stock mínimo")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f"{self.product.name} - {self.quantity} en stock"

    def is_low_stock(self):
        return self.quantity <= self.min_stock

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES, verbose_name="Tipo de transacción")
    quantity = models.PositiveIntegerField(verbose_name="Cantidad")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de transacción")
    note = models.TextField(blank=True, null=True, verbose_name="Nota")
    exported = models.BooleanField(default=False, verbose_name="Exportado a Excel/PDF")

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.product.name} ({self.quantity})"
