from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class RecipeViewList(generic.ListView):
    template_name = 'dishes/recipe_list.html'
    context_object_name = 'recipe'
    model = models.Recipe
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
class RecipeDetail(generic.DetailView):
    template_name = 'dishes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.object.recipe.all() 
        return context

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)

class AddRecipe(generic.CreateView):
    template_name = 'dishes/add_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_list/'
    
    def form_valid(self, form):
        return super(AddRecipe, self).form_valid(form=form)
         
    
class AddIngredient(generic.CreateView):
    template_name = 'dishes/add_ingredient.html'
    form_class = forms.IngredientForm
    success_url = '/recipe_list/'
    
    def form_valid(self, form):
        return super(AddIngredient, self).form_valid(form=form)
       

class DeleteFromRecipe(generic.DeleteView):
    template_name = 'dishes/confirm_delete.html'
    success_url = '/recipe_list/'
    
    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id = recipe_id)
    
