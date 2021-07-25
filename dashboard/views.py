from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = Order.objects.filter(is_accepted=False).count()
    product_count = products.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashhome')
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'form':form,
        'products':products,
        'product_count': product_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
    }
    return render(request,'dashboard/home.htm/',context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.filter(is_accepted=False).count()
    product_count = Product.objects.all().count() 
    context = {
        'workers': workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
    }
    return render(request,'dashboard/staff.htm', context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request,'dashboard/staff_detail.htm', context)

@login_required
def product(request):
    items = Product.objects.all()
    product_count = items.count()
    orders_count = Order.objects.filter(is_accepted=False).count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashproduct')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'product_count': product_count,
        'orders_count': orders_count,
        'workers_count': workers_count,
    }
    return render(request,'dashboard/product.htm', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashproduct')
    return render(request,'dashboard/product_delete.htm')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashproduct')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request,'dashboard/product_update.htm', context)


@login_required
def order(request):
    orders = Order.objects.filter(is_accepted=False)
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'orders': orders,
        'orders_count': orders_count,
        'workers_count': workers_count,
        'product_count': product_count,
    }
    return render(request,'dashboard/order.htm', context)


