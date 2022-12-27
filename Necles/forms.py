from  django import forms
from Necles.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        exclude =['tag']