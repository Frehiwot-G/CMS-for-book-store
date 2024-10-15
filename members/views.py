from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from .models import *
from .forms import NewMemberForm,OrderForm,CustomerForm,BookForm, OrderFormCustomer

from .filters import OrderFilter
from .decoraters import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def homePage(request):
    order=Order.objects.all()
    customer=Customer.objects.all()
    # b=order.filter(book=customer.objects.name)
    

    total_orders=order.count()
    total_customers=customer.count()
    delivered= order.filter(status='delivered').count()
    pending= order.filter(status='pending').count()
    context={'orders':order,'customers':customer,'total_orders':total_orders,'total_customers':total_customers,
    'delivered':delivered,'pending':pending}
    return render(request, 'home.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders=request.user.customer.order_set.all()
    total_orders=orders.count()
    delivered= orders.filter(status='delivered').count()
    pending= orders.filter(status='pending').count()
    context={'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def account_setting(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid:
            form.save()
    context={'form':form}
    return render(request, 'member_setting.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def bookPage(request):
    books=Book.objects.all()
    return render(request, 'books.html',{'books':books})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customerPage(request,pk):
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    order_count=order.count()

    myfilter=OrderFilter(request.GET, queryset=order)
    order=myfilter.qs

    context={'customer':customer,'order':order,'order_count':order_count, 'myfilter':myfilter}
    return render(request, 'customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    # OrderFormSet=inlineformset_factory(Customer,Order,fields=('book','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    # form=OrderFormSet(instance=customer)
    form=OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form=OrderForm(request.POST)
        # form=OrderFormSet(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    # context={'form':form}
    context={'form':form}
    return render(request,'create_order.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createOrderCustomer(request):
    # OrderFormSet=inlineformset_factory(Customer,Order,fields=('book','status'),extra=10)
    # customer=Customer.objects.get(id=pk)
    customer=request.user.customer
    # form=OrderFormSet(instance=customer)
    form=OrderFormCustomer(initial={'customer':customer})
    if request.method == 'POST':
        form=OrderFormCustomer(request.POST)
        # form=OrderFormSet(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    # context={'form':form}
    context={'form':form}
    return render(request,'create_order.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    # form=OrderForm()
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'create_order.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'delete.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def register_bookPage(request):
    form =BookForm()
    if request.method == 'POST':
        form =BookForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Book was registered.')
            return redirect('book')

    context={'form':form}
    return render(request, 'register_book.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateBook(request,pk):
    # form=OrderForm()
    book=Book.objects.get(id=pk)
    form=BookForm(instance=book)
    if request.method == 'POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')
    context={'form':form}
    return render(request,'register_book.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteBook(request,pk):
    book=Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book')
    context={'item':book}
    return render(request,'delete_book.html',context)


@unauthenticated_user
def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form =NewMemberForm()
    if request.method == 'POST':
        form =NewMemberForm(request.POST) 
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group= Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            messages.success(request, 'account was created for' + username)
            return redirect('login')

    context={'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            
    context={}
    return render(request, 'login.html', context)
def logoutuser(request):
    logout(request)
    return redirect('login')
