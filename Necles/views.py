from django.shortcuts import render,redirect
from  django.http import HttpResponse
from Necles.models import  Customer,Necklace,Order
from Necles.forms import OrderForm
from django.forms import inlineformset_factory
from Necles.filters import OrderFilter
from django.contrib.auth.decorators import login_required
from Necles.decorators import notloguser,ForAdminOnly,alloweduser

# Create your views here.


#                                            Base App
@login_required(login_url='/user/login/')
@ForAdminOnly
def home(request):
    customr=Customer.objects.all()
    orders=Order.objects.all()
    t_order=orders.count()
    out_order=orders.filter(status='out_of_order').count()
    p_order=orders.filter(status='Pending').count()
    d_order = orders.filter(status='Delivered').count()
    in_order = orders.filter(status='in_progress').count()
    out_stock_order = orders.filter(status='out_of_stock').count()

    context={'customr':customr,
             'orders':orders,
             'out_order':out_order,
             'p_order':p_order,
             'd_order':d_order,
             'in_order':in_order,
             't_order':t_order,
             'out_stock_order':out_stock_order}

    return render(request,'nec/home.html',context)

@login_required(login_url='/user/login/')
def product(request):
    product=Necklace.objects.all()

    return render(request, 'nec/about.html', {'product':product})

@login_required(login_url='/user/login/')
@ForAdminOnly
def Custumer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    serchfilter=OrderFilter(request.GET,queryset=orders)
    orders=serchfilter.qs
    return render(request, 'nec/Custumer.html', {'customer':customer,'orders':orders,'serchfilter':serchfilter})

#                                            Product CUD
@login_required(login_url='/user/login/')
@alloweduser(allowegroups=['customer'])
def create(request,pk):
    OrderformSet=inlineformset_factory(Customer,Order,fields=('iteam','status'))
    customer=Customer.objects.get(id=pk)
    formset=OrderformSet(queryset=Order.objects.none(),instance=customer)
    if request.method=='POST':
        formset=OrderformSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return  redirect('home')

    return render(request,'my_forms.html',{'formset':formset})

@login_required(login_url='/user/login/')
def update(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return  redirect('home')
    context={'form':form}
    return render(request,'update.html',context)

@login_required(login_url='/user/login/')
@ForAdminOnly
def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context={'order':order}
    return render(request,'delete_form.html',context)

