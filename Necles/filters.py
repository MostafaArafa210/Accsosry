import django_filters
from Necles.models import  Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['iteam','status']
