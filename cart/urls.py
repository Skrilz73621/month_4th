from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/', views.AddToCart.as_view(), name='add_to_cart'),
    path('cart_list/', views.CartList.as_view(), name='cart_list'),
    path('cart_list/<int:id>/', views.CartDetail.as_view(), name='cart_detail'),
    path('cart_list/<int:id>/update/', views.ChangeCart.as_view(), name='change_in_cart'),
    path('cart_list/<int:id>/delete/', views.DeleteFromCart.as_view(), name='delete_from_cart')
]
