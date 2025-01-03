from django.shortcuts import render
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