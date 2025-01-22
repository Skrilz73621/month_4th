from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models
from django.views import generic
from django.http import HttpResponse
import datetime
from . import forms
    
# def book_list(request):
#     if request.method == 'GET':
#         book_list = models.Books.objects.all().order_by('-id')
#         context = {'book_list':book_list}
#         return render(request, context=context, template_name='book.html')


class BookList(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Books
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
# def book_detail(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(models.Books, id=id)
#         context = {'book': book}
#         return render(request, context=context, template_name='book_detail.html')


class BookDetail(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id = todo_id)


class AddReview(generic.CreateView):
    template_name = 'add_review.html'
    form_class = forms.ReviewForm
    success_url = '/'
    
    def form_valid(self, form):
        return super(AddReview, self).form_valid(form=form)
    
    
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context