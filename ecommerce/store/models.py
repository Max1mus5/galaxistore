from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=255) # Guardar la ruta de las imágenes como texto
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField()

    def __str__(self):
        return self.nombre

class ProductoEnCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
