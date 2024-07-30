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




#def confirm_payment(request, pk):
#    cart = Cart.objects.get(id=pk)
#    cart.completed = True
#    cart.save(0)
#    messages.success(request, "payment made successfully")
#    return redirect("index")
