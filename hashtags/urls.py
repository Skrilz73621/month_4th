from django.urls import path
from . import views

urlpatterns = [
    path('all_products', views.AllProducts.as_view(), name='all_products'),
    path('drama', views.Drama.as_view(), name='drama'),
    path('fantasy', views.Fantasy.as_view(), name='fantasy'),
    path('fairy_tale', views.FairyTale.as_view(), name='fairy_tale'),
]
