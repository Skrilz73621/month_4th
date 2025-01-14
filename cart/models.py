from django.db import models

class CartModel(models.Model):
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} --- {self.created_at}'
