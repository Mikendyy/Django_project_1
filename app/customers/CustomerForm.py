from django.forms import ModelForm
from customers.models import Customer

class CustomerFormForCreate(ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "age", "city", "email", "business")
