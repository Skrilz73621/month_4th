from django.contrib import admin
from . import models

admin.site.register(models.Ingredient)
admin.site.register(models.Recipe)

# Register your models here.
