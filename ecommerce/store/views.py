from django.shortcuts import render
from .models import Producto, ProductoEnCarrito
from .cart import Cart

def store(request): 
    productos = Producto.objects.all() # Obtener todos los productos de la tienda
    context = {'productos': productos} # Pasar los productos al contexto
    return render(request, 'store/store.html', context)
    
def cart(request):
    # Inicializar el carrito
    cart = Cart(request)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']
    
    # Para usuarios no autenticados, utilizar el carrito de la sesión
    if not request.user.is_authenticated:
        items_en_carrito = []
        total = 0
        for product_id, quantity in cart.cart.items():
            producto = Producto.objects.get(id=product_id) # Obtener el producto por id
            subtotal = producto.precio * quantity # Calcular el subtotal para este producto
            total += subtotal # Sumar al total
            item = ProductoEnCarrito(nombre=producto.nombre, imagen=producto.imagen, cantidad=quantity, precio=producto.precio, total=subtotal)
            items_en_carrito.append(item) # Añadir al carrito
        context = {'items_en_carrito': items_en_carrito, 'total': total, 'cartItems': cartItems}
    else:
        context = {'items': items, 'order': order, 'cartItems': cartItems}
    
    return render(request, 'store/cart.html', context)



def checkout(request):
    items_en_carrito = ProductoEnCarrito.objects.all() # Obtener todos los productos en el carrito
    total = sum(item.total for item in items_en_carrito) # Calcular el total de la compra
    context = {'items_en_carrito': items_en_carrito, 'total': total} # Pasar los productos y el total al contexto
    return render(request, 'store/checkout.html', context)
