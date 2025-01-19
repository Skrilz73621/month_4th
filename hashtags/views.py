from django.shortcuts import render
from . import models
from django.views import generic

# Общий список продуктов
# def all_products(request):
#     if request.method == 'GET':
#         all_products = models.Products.objects.all()
#         context = {'all_products':all_products}
#         return render(request, template_name='hashtags/all_products.html', context=context)

class AllProducts(generic.ListView):
    template_name = 'hashtags/all_products.html'
    context_object_name = 'all_products'
    model = models.Products
    
    def get_queryset(self, **kwargs):
        return self.model.objects.all().order_by('id')

# напитки 
# def drama(request):
#     if request.method == "GET":
#         drama = models.Products.objects.filter(tags__name='Драма')
#         context = {'drama':drama}
#         return render(request, context=context, template_name='hashtags/drama.html')

class Drama(generic.ListView):
    template_name = 'hashtags/drama.html'
    context_object_name = 'drama'
    model = models.Products
    
    def get_queryset(self, **kwargs):
        return models.Products.objects.filter(tags__name = 'Драма')
    
    
class Fantasy(generic.ListView):
    template_name = 'hashtags/fantasy.html'
    context_object_name = 'fantasy'
    model = models.Products
    
    def get_queryset(self, **kwargs):
        return models.Products.objects.filter(tags__name = 'Фантастика')
    
    
class FairyTale(generic.ListView):
    template_name = 'hashtags/fairy_tale.html'
    context_object_name = 'fairy_tale'
    model = models.Products
    
    def get_queryset(self, **kwargs):
        return models.Products.objects.filter(tags__name = 'Сказки')