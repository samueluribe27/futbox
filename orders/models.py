from django.db import models
from products.models import Product
from users.models import User


class Order(models.Model):
    status = [
        ('pending','Pendiente'),
        ('shipped','Enviado'),
        ('delivered','Entregado')
    ]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=status, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return f"Orden {self.id} - {User.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        self.total = Product.price * self.quantity
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.quantity} x {Product.name} en {self.order.id}"

