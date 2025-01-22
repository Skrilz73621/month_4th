from django.urls import path
from . import views

urlpatterns = [
    path('parsed_book/', views.ParsedBookList.as_view(), name='parsed_book'),
    path('parsed_form/', views.ParsedBookForm.as_view(), name='parsed_form')
]
