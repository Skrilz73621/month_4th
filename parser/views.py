from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms
from django.views import generic


class ParsedBookList(generic.ListView):
    template_name = 'parsed/parsed_books.html'
    context_object_name = 'parse'
    model = models.BookParser
    
    def get_queryset(self):
        return self.model.objects.all()
    
class ParsedBookForm(generic.FormView):
    template_name = 'parsed/parsed_form.html'
    form_class = forms.ParserForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг прошел успешно')
        else:
            return super(ParsedBookForm, self).post(request, *args, **kwargs)
    