from django.db import models
from library.models import Books


class CartModel(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)  # Пример default=1
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} --- {self.created_at}'
