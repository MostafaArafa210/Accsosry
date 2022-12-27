
from django.urls import path,include
from . import  views
urlpatterns = [
#                    BAse
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('custumer/<str:pk>', views.Custumer, name='custumer'),

    # path('create', views.create, name='create'),
#                    CRD
    path('create/<str:pk>', views.create, name='create'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),

]
