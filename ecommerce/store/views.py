from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
import datetime
import json
from .models import *

def error_view(request):
    return render(request, 'store/error.html')

def signup(request):
    form = UserCreationForm() # Inicializa 'form' aquí para asegurarte de que esté definida en todos los caminos
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                Customer.objects.create(
                    user=user,
                    name=user.username,  
                    email=None
                )
                return redirect('user_login')  
    except Exception as e:
        return error_view(request)
    return render(request, 'store/signup.html', {'form': form})



def user_login(request):
    form = AuthenticationForm() # Inicializa 'form' aquí para asegurarte de que esté definida en todos los caminos
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('store')  
    return render(request, 'store/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('store')

def store(request): 
    try:
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
        productos = Producto.objects.all() 
        context = {'productos': productos} 
        return render(request, 'store/store.html', context)
    except Exception as e:
        return error_view(request)

    

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
    try:
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
    except Exception as e:
        return error_view(request)

def updfateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    customer = request.user.customer
    product = Producto.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
    )
    orderItem, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    if orderItem.quantity < 1:
        orderItem.delete()
    else:
        orderItem.save()

    order.get_cart_total
    return JsonResponse(
        'Item was updated',
        safe=False
    )


def processOrder(request):
    try:
        print('Data:', request.body)
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, _ = Order.objects.get_or_create(
                customer=customer,
                complete=False
            )
            total = float(data['form']['total'])
            order.transaction_id = transaction_id
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
            return JsonResponse('Payment complete!', safe=False)  # JSON back
    except Exception as e:
        return error_view(request)
   