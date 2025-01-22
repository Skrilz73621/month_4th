from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetail.as_view(), name='book_detail'),
    path('add_review/', views.AddReview.as_view(), name='add_review'),
    path('search/', views.SearchView.as_view(), name='search')
]
