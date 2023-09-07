from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    staffs=User.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff =  request.user  #assigning a user to the request made
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    count_order=orders.count()
    count_product=products.count()
    count_staff=staffs.count()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'count_order':count_order,
        'count_product':count_product,
        'count_staff':count_staff,
    }
    return render(request, 'dashboard/index.html', context)

# staffs
@login_required
def staff(request):
    workers = User.objects.all()
    count_staff=workers.count()
    count_order=Order.objects.all().count()
    count_product=Product.objects.all().count()
    context={
        'workers': workers,
        'count_product': count_product,
        'count_staff': count_staff,
        'count_order': count_order,

    }
    return render(request, 'dashboard/staff.html', context)

# staff details
@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    count_product=Product.objects.all().count()
    count_staff=workers.count()
    count_order=Order.objects.all().count()
    context={
        'workers':workers,   
        'count_product':count_product, 
        'count_staff': count_staff,
        'count_order': count_order,
  
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    items = Product.objects.all() # Using object relational mapping(ORM) 
    # items = Product.objects.raw('SELECT * FROM dashboard_product') #USING Normalsql statement
    if request.method=='POST':
       form = ProductForm(request.POST)
       if form.is_valid():
           form.save()
           product_name = form.cleaned_data.get('name')
           messages.success(request, f'{product_name} has been added')
           return redirect('dashboard-product')
    else:
       form = ProductForm()
    count_product=items.count()  
    count_staff=User.objects.all().count()
    count_order=Order.objects.all().count()
    context ={
        'items': items,
        'form': form,
        'count_product': count_product,
        'count_staff': count_staff,
        'count_order': count_order,
        
    }
    return render(request, 'dashboard/product.html', context)

#update a product
@login_required
def product_update(request, pk):
    selected_item = Product.objects.get(id=pk)
    if request.method== 'POST':
        form= ProductForm(request.POST, instance=selected_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form= ProductForm(instance=selected_item)
        
    context ={
        'form':form
    }
    return render(request, 'dashboard/product_update.html', context)

# delete a product 
@login_required 
def product_delete(request, pk):
    selected_item = Product.objects.get(id=pk)
    if request.method=='POST':
        selected_item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

# Orders
@login_required
def order(request):
    orders=Order.objects.all()
    count_product=Product.objects.all().count()
    count_staff=User.objects.all().count()
    count_order=orders.count
    context={
        'orders':orders,
        'count_order':count_order,
        'count_staff':count_staff,
        'count_product': count_product,
        
    }
    return render(request, 'dashboard/order.html', context)

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')