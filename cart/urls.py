from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_list/', views.cart_list, name='cart_list'),
    path('cart_list/<int:id>/', views.cart_detail, name='cart_detail'),
    path('cart_list/<int:id>/update/', views.change_cart, name='change_in_cart'),
    path('cart_list/<int:id>/delete/', views.delete_from_cart, name='delete_from_cart')
]
