from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

# def add_to_cart(request):
#     if request.method == 'POST':
#         form = forms.CartForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = forms.CartForm()
#     return render(request, template_name='cart/add_to_cart.html', context={'form':form})

class AddToCart(generic.CreateView):
    template_name = 'cart/add_to_cart.html'
    form_class = forms.CartForm
    success_url = '/cart_list/'
    
    def form_valid(self, form):
        return super(AddToCart, self).form_valid(form=form)

# def cart_detail(request, id):
#     if request.method == 'GET':
#         cart_id = get_object_or_404(models.CartModel, id=id)
#         context = {'cart_id':cart_id}
#         return render(request, template_name='cart/cart_detail.html', context=context)

class CartDetail(generic.DetailView):
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart_id'
    
    def get_object(self, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.CartModel, id = cart_id)
    

# def cart_list(request):
#     if request.method == 'GET':
#         cart_list = models.CartModel.objects.all().order_by('-id')
#         context = {'cart_list':cart_list}
#         return render(request, template_name='cart/cart_list.html', context=context)

class CartList(generic.ListView):
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart_list'
    model = models.CartModel
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    


# def delete_from_cart(request, id):
#     cart_id = get_object_or_404(models.CartModel, id=id)
#     cart_id.delete()
#     return redirect('cart_list')

class DeleteFromCart(generic.DeleteView):
    template_name = 'cart/confirm_delete.html'
    success_url = '/cart_list/'
    
    def get_object(self, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.CartModel, id = cart_id)
    
    
# def change_cart(request, id):
#     cart_id = get_object_or_404(models.CartModel, id=id)
#     if request.method == 'POST':
#         form = forms.CartForm(request.POST, instance=cart_id)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_list')
#     else:
#         form = forms.CartForm(instance=cart_id)
#     return render(request, template_name='cart/change_in_cart.html', context={'form':form})


class ChangeCart(generic.UpdateView):
    template_name = 'cart/change_in_cart.html'
    form_class = forms.CartForm
    success_url = '/cart_list/'
    
    def get_object(self, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.CartModel, id=cart_id)
    
    def form_valid(self, form):
        return super(ChangeCart, self).form_valid(form)