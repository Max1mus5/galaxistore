from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
import datetime
import json
from .models import *

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                name=user.username,  # Puedes establecer el nombre como el nombre de usuario por defecto
                email=None
            )
            return redirect('user_login')  # Redirigir al usuario al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('store')  # Redirigir al usuario a la página principal después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('store')

def store(request): 
    if request.user.is_authenticated:
        print("request.user*****************************************************",request.user.is_authenticated)
        print("user*****************************************************",request.user)
        customer = request.user.customer
        print("customer*****************************************************",customer)
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    productos = Producto.objects.all() # Obtener todos los productos de la tienda
    context = {'productos': productos} # Pasar los productos al contexto
    return render(request, 'store/store.html', context)

    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
        )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        productos = Producto.objects.all()
        context = {'productos':productos, 'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'store/cart.html', context)
    else:
       
       return redirect('signup')
   
   


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        try:
            order = Order.objects.get(id=OrderItem.order_id)
            order.orderitem_set.all().delete()
        except Order.DoesNotExist:
            print("El pedido no existe.")
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def updfateItem(request):
    # Se carga el JSON de la solicitud
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    # Se obtiene el cliente autenticado
    customer = request.user.customer
    
    # Se obtiene el producto
    product = Producto.objects.get(id=productId)
    
    # Se obtiene o crea el pedido para el cliente actual
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
    )
    
    # Se obtiene o crea el item del pedido para el producto actual
    orderItem, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    # Si el action es 'add', se aumenta la cantidad del item en 1
    if action == 'add':
        orderItem.quantity += 1
    # Si el action es 'remove', se disminuye la cantidad del item en 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    # Si la cantidad del ítem es menor que 1, se elimina el ítem del carrito
    if orderItem.quantity < 1:
        orderItem.delete()
    else:
        # Guarda los cambios en el item del pedido
        orderItem.save()

    order.get_cart_total
    # Retorna un JSON con un mensaje indicando que el item fue actualizado
    return JsonResponse(
        'Item was updated',
        safe=False
    )


# Ahora vamos haces una funcion para procesar el pedido
def processOrder(request):
    print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        # Verificar que no se este intentando hacer un pedido falso
        if abs(total - order.get_cart_total) < 0.001:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in')
    return JsonResponse('Payment complete!', safe=False) # Retorna un JSON