from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,authenticate
from user.forms import CustoumerForm,CreateNewUser
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate,decorators
from django.contrib.auth.decorators import login_required
from Necles.decorators import notloguser,alloweduser
from Necles.models import Customer,Order
import requests
from django.conf import settings

# Create your views here.

@notloguser
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateNewUser(request.POST)
        if request.method=="POST":
            form = CreateNewUser(request.POST)
            if form.is_valid():
                recaptcha_response=request.POST.get('g-recaptcha-response')
                data={
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response':recaptcha_response
                }
                r=requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                resualt=r.json()
                if resualt['success']:
                    user= form.save()
                    username=form.cleaned_data.get('username')
                    messages.success(request,username + 'Created Succsessfly')
                    return redirect('login')
                else:
                    messages.error(request,'invaild recaptcha ples try again')

        context={'form':form}
        return render(request,'auth/register.html',context)


@notloguser
def log_in(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        resualt = r.json()
        if user is not None and resualt['success']:
               login(request,user)
               return redirect('profile')
        else:
                messages.info(request,  'Creditnon Erorr')
                messages.error(request, 'invaild recaptcha ples try again!')
                return redirect('login')
    context={}
    return render(request,'auth/login.html',context)



def log_out(request):
    logout(request)

    return redirect('login')

@login_required(login_url='login')
@alloweduser(allowegroups=['customer'])
def profile(request):
    customer=request.user.customer.order_set.all()
    orders = Order.objects.all()
    t_order = customer.count()
    out_order = customer.filter(status='out_of_order').count()
    p_order = customer.filter(status='Pending').count()
    d_order = customer.filter(status='Delivered').count()
    in_order = customer.filter(status='in_progress').count()
    out_stock_order = customer.filter(status='out_of_stock').count()
    context = {
               'order':customer,
               'out_order': out_order,
               'p_order': p_order,
               'd_order': d_order,
               'in_order': in_order,
               't_order': t_order,
               'out_stock_order': out_stock_order}
    # context={}
    return render(request,'auth/profile.html',context)

@login_required(login_url='login')
def profile_info(request):
    pic=Customer.objects.get(user=request.user)
    customer=request.user.customer
    form=CustoumerForm(instance=customer)
    if request.method=='POST':
        form = CustoumerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context={'form':form,'pic':pic}
    return render(request,'auth/profile_info.html',context)
