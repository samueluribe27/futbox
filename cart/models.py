from django.db import models
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"carrito de {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} en carrito"
    
    def calcularTotal(self, *args, **kwargs):
        self.total = Product.price * self.quantity