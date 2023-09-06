from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

# staffs
@login_required
def staff(request):
    workers = User.objects.all()
    context={
        'workers': workers,
    }
    return render(request, 'dashboard/staff.html', context)

# staff details
@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context={
        'workers':workers,   
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
           return redirect('dashboard-product')
    else:
       form = ProductForm()
       
    context ={
        'items': items,
        'form': form,
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
    cart =Product.objects.all()
    context={
        'orders':orders,
        'cart': cart,
        
    }
    return render(request, 'dashboard/order.html', context)

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')