from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models
from django.http import HttpResponse
import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Hello, this is "about me" page')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('Hello, this is "about_my_pets" page')
    
def date_time(request):
    if request.method == 'GET':
        i = datetime.datetime.now()
        return HttpResponse(f'Hello, this is "date_time" page, {i}') 
    
def book_list(request):
    if request.method == 'GET':
        book_list = models.Books.objects.all().order_by('-id')
        context = {'book_list':book_list}
        return render(request, context=context, template_name='book.html')
    
def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(models.Books, id=id)
        context = {'book': book}
        return render(request, context=context, template_name='book_detail.html')

