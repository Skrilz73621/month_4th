from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def add_to_cart(request):
    if request.method == 'POST':
        form = forms.CartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = forms.CartForm()
    return render(request, template_name='cart/add_to_cart.html', context={'form':form})

def cart_detail(request, id):
    if request.method == 'GET':
        cart_id = get_object_or_404(models.CartModel, id=id)
        context = {'cart_id':cart_id}
        return render(request, template_name='cart/cart_detail.html', context=context)
    

def cart_list(request):
    if request.method == 'GET':
        cart_list = models.CartModel.objects.all().order_by('-id')
        context = {'cart_list':cart_list}
        return render(request, template_name='cart/cart_list.html', context=context)


def delete_from_cart(request, id):
    cart_id = get_object_or_404(models.CartModel, id=id)
    cart_id.delete()
    return redirect('cart_list')
    
    
def change_cart(request, id):
    cart_id = get_object_or_404(models.CartModel, id=id)
    if request.method == 'POST':
        form = forms.CartForm(request.POST, instance=cart_id)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = forms.CartForm(instance=cart_id)
    return render(request, template_name='cart/change_in_cart.html', context={'form':form})