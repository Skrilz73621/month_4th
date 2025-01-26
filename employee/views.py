from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import models, forms

class RegisterView(generic.CreateView):
    form_class = forms.CustomEmployeeForm
    template_name = 'employee/register.html'
    success_url = reverse_lazy('employee:login')
    
class AuthLoginView(LoginView):
    template_name = 'employee/login.html'
    form_class = AuthenticationForm
        
    def get_success_url(self):
        return reverse('employee:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('employee:login')
    

class UserListView(generic.ListView):
    template_name = 'employee/user_list.html'
    context_object_name = 'employee_list'
    model = models.CustomEmployee
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
