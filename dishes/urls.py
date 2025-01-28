from django.urls import path
from . import views

urlpatterns = [
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('add_ingredient/', views.AddIngredient.as_view(), name='add_ingredient'),
    path('recipe_list/', views.RecipeViewList.as_view(), name='recipe_list'),
    path('recipe_list/<int:id>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe_list/<int:id>/delete/', views.DeleteFromRecipe.as_view(), name='delete_from_recipe')
]
