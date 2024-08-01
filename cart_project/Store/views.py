from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login
import uuid
# Create your views here.



def index(request):
    products = Product.objects.all()
    
    context = {"products":products}
    return render(request, "index.html", context)


def cart(request):
    
    context = {}
    return render(request, "cart.html", context)

def add_to_cart(request):
    data = json.load(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
       cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
       cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
       cartitem.quantity += 1
       cartitem.save()
       print(cartitem)
    return JsonResponse("it worked", safe=False)




#def confirm_payment(request, pk):
#    cart = Cart.objects.get(id=pk)
#    cart.completed = True
#    cart.save(0)
#    messages.success(request, "payment made successfully")
#    return redirect("index")
