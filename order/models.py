from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    SIZE_CHOICE = (
        ('SMALL','small'),
        ('LARGE','Large'),
        ('EXTRA_LARGE','Extra Large'),
    )
    size = models.CharField(max_length=20,choices=SIZE_CHOICE,default=[0][0])
    ORDER_STATUS = (
        ('PENDING','Pending'),
        ('IN_TRANSIT','Transit'),
        ('DELIVERED','Delivered'),
    )
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default=[0][0])
    quantity = models.IntegerField()
    email = models.EmailField(max_length=80)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"
