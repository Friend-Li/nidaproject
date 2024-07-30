from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="img", default="")


    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    

