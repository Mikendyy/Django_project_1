from django.urls import path
from customers.views import CustomerListView
from customers.views import CustomerDetalesView
from customers.views import CustomerCreateView
from customers.views import CustomerUpdateView
from customers.views import CustomerDeleteView

urlpatterns = [
    path('customer-list/', CustomerListView.as_view(), name="customer-list-link"),
    path('customer-details/<int:pk>', CustomerDetalesView.as_view(), name='customer-details-link'),
    path('customer-create/', CustomerCreateView.as_view(), name="customer-create-link"),
    path('customer-update/<int:pk>', CustomerUpdateView.as_view(), name='customer-update-link'),
    path('customer-delete/<int:pk>', CustomerDeleteView.as_view(), name="customer-delete-link"),
]
