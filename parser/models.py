from django.db import models

# Create your models here.

class BookParser(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='book_sheet/')
    
    def __str__(self):
        return self.title