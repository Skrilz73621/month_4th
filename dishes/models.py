from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    UNIT = (
        ('Г','Грамм'),
        ('Кг','Килограмм'),
        ('Мл','Миллилитр'),
        ('Л','Литр'),
        ('Шт','Штука')
    )
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(choices=UNIT, max_length=10)
    
    def __str__(self):
        return f'{self.name} - {self.unit}'
    
