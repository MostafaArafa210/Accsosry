from django.contrib import admin

# Register your models here.
from Necles.models import Customer,Order,Necklace,Tag
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Necklace)
admin.site.register(Tag)
