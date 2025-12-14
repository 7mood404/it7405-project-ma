from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES = [
    ('Cart', 'Cart'),
    ('Pending', 'Pending'),
    ('Successful', 'Successful'),
    ('Failed', 'Failed'),
    ('Cancelled', 'Cancelled'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status} - {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20)   # sandwich / meal
    drink = models.CharField(max_length=50, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} x{self.quantity}"