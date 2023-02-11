from customers.models import Customer
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from customers.CustomerForm import CustomerFormForCreate

class CustomerListView(ListView):
    model = Customer
    template_name = 'customerList.html'

class CustomerDetalesView(DetailView):
    model = Customer
    template_name = 'customerDetails.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerFormForCreate
    success_url = reverse_lazy("customer-list-link")
    template_name = 'customerCreate.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerFormForCreate
    success_url = reverse_lazy("customer-list-link")
    template_name = 'customerUpdate.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer-list-link")
    template_name = 'customerDelete.html'

class Home(TemplateView):
    template_name = 'index.html'