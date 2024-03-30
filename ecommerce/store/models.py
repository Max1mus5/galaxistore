from django.db import models
from django.contrib.auth.models import User

# Ahora construiremos el modelo de Customer
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=255) # Guardar la ruta de las imágenes como texto
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField()

    def __str__(self):
        return self.nombre

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    # Ahora necesitamos agregar una propiedad que nos determine si hay que enviar el pedido
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        shipping = True 
        return shipping

    # Ahora vamos a anadir propiedades para obtener el total de la orden y el total de items
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # Ahora vamos a anadir una propiedad para obtener el total del item
    @property
    def get_total(self):
        total = self.product.precio * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address