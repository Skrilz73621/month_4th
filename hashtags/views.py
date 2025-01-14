from django.shortcuts import render
from . import models

# Общий список продуктов
def all_products(request):
    if request.method == 'GET':
        all_products = models.Products.objects.all()
        context = {'all_products':all_products}
        return render(request, template_name='hashtags/all_products.html', context=context)

# напитки 
def drama(request):
    if request.method == "GET":
        drama = models.Products.objects.filter(tags__name='Драма')
        context = {'drama':drama}
        return render(request, context=context, template_name='hashtags/drama.html')
    
    
def fantasy(request):
    if request.method == "GET":
        fantasy = models.Products.objects.filter(tags__name='Фантастика')
        context = {'fantasy':fantasy}
        return render(request, context=context, template_name='hashtags/fantasy.html')
    
    
def fairy_tale(request):
    if request.method == "GET":
        fairy_tale = models.Products.objects.filter(tags__name='Сказки')
        context = {'fairy_tale':fairy_tale}
        return render(request, context=context, template_name='hashtags/fairy_tale.html')