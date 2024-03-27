from django.shortcuts import render,redirect,get_object_or_404
# from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from customer.models import *
from customer.forms import *
from .models import *
from .forms import *

#for showing login button for admin
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('businesslogin')

def business_signup_view(request):
    business_userForm=BusinessUserForm()
    businessForm =BusinessForm()
    mydict={'business_userForm':business_userForm,'businessForm':businessForm}
    if request.method=='POST':
        business_userForm=BusinessUserForm(request.POST)
        businessForm =BusinessForm(request.POST,request.FILES)
        if business_userForm.is_valid() and businessForm.is_valid():
            user=business_userForm.save()
            user.set_password(user.password)
            user.save()
            business=businessForm.save(commit=False)
            business.user=user
            business.save()
            business_group = Group.objects.get_or_create(name='BUSINESS')
            business_group[0].user_set.add(user)
        return HttpResponseRedirect('businesslogin')
    return render(request,'business/business_signup.html',context=mydict)

#-----------for checking user isbusiness
def is_business(user):
    return user.groups.filter(name='BUSINESS').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF BUSINESS
# def afterlogin_view(request):
#     if is_business(request.user):
#         return redirect('business-dashboard')
#     else:
#         return redirect('business-dashboard')

#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='businesslogin')
def business_dashboard_view(request):
    # for cards on dashboard
    business = Business.objects.get(user=request.user)
    customercount=Customer.objects.all().count()
    products=Product.objects.filter(business=business)
    orders=Orders.objects.filter(product__in=products)

    # for recent order tables
    # orders=Orders.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=Product.objects.all().filter(id=order.product.id)
        ordered_by=Customer.objects.all().filter(id = order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)

    mydict={
    'customercount':customercount,
    'productcount':products.count(),
    'ordercount':orders.count(),
    'data':zip(ordered_products,ordered_bys,orders),
    }
    return render(request,'business/business_dashboard.html',context=mydict)

# admin view customer table
@login_required(login_url='businesslogin')
def business_view_customer_view(request):
    customers=Customer.objects.all()
    return render(request,'business/view_customer.html',{'customers':customers})

# admin delete customer
@login_required(login_url='businesslogin')
def business_delete_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('view-customer')


@login_required(login_url='businesslogin')
def business_update_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    userForm=CustomerUserForm(instance=user)
    customerForm=CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=CustomerUserForm(request.POST,instance=user)
        customerForm=CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-customer')
    return render(request,'business/business_update_customer.html',context=mydict)

# admin view the product
@login_required(login_url='businesslogin')
def business_products_view(request):
    products=Product.objects.filter(business__user=request.user)
    return render(request,'business/business_products.html',{'products':products})


# admin add product by clicking on floating button
@login_required(login_url='businesslogin')
def business_add_product_view(request):
    if request.method=='POST':
        productForm=ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            product = productForm.save(commit=False)
            business = Business.objects.get(user=request.user)
            product.business = business
            product.save()
        return HttpResponseRedirect('business-products')
    else:
        productForm=ProductForm()
    return render(request,'business/business_add_products.html',{'productForm':productForm})


@login_required(login_url='businesslogin')
def business_delete_product_view(request,pk):
    product=get_object_or_404(Product,id=pk, business__user=request.user)
    if product.owner == request.user:
        product.delete()
        return redirect('business-products')


@login_required(login_url='businesslogin')
def business_update_product_view(request,pk):
    product=get_object_or_404(Product,id=pk, business__user=request.user)
    productForm=ProductForm(instance=product)
    if request.method=='POST':
        productForm=ProductForm(request.POST,request.FILES,instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('business-products')
    return render(request,'business/business_update_product.html',{'productForm':productForm})


@login_required(login_url='businesslogin')
def business_view_booking_view(request):
    business = Business.objects.get(user=request.user)
    products=Product.objects.filter(business=business)
    orders=Orders.objects.filter(product__in=products)
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=Product.objects.all().filter(id=order.product.id)
        ordered_by=Customer.objects.all().filter(id = order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request,'business/business_view_booking.html',{'data':zip(ordered_products,ordered_bys,orders)})


@login_required(login_url='businesslogin')
def business_delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('business-view-booking')

# for changing status of order (pending,delivered...)
@login_required(login_url='businesslogin')
def business_update_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    orderForm=OrderForm(instance=order)
    if request.method=='POST':
        orderForm=OrderForm(request.POST,instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('business-view-booking')
    return render(request,'business/update_order.html',{'orderForm':orderForm})


# admin view the feedback
@login_required(login_url='businesslogin')
def business_view_feedback_view(request):
    feedbacks=Feedback.objects.all().order_by('-id')
    return render(request,'business/view_feedback.html',{'feedbacks':feedbacks})


@login_required(login_url='businesslogin')
@user_passes_test(is_business)
def business_profile_view(request):
    business=Business.objects.get(user_id=request.user.id)
    return render(request,' business/business_profile.html',{'business':business})


@login_required(login_url='businesslogin')
@user_passes_test(is_business)
def business_edit_profile_view(request):
    business=Business.objects.get(user_id=request.user.id)
    businessuser=User.objects.get(id=business.user_id)
    businessuserForm=BusinessUserForm(instance=businessuser)
    businessForm=BusinessForm(request.FILES,instance=business)
    mydict={'businessuserForm':businessuserForm,'businessForm':businessForm}
    if request.method=='POST':
        businessuserForm=BusinessUserForm(request.POST,instance=businessuser)
        businessForm=BusinessForm(request.POST,instance=business)
        if businessuserForm.is_valid() and businessForm.is_valid():
            businessuser=businessuserForm.save()
            businessuser.set_password(businessuser.password)
            businessuser.save()
            businessForm.save()
            return HttpResponseRedirect('business-profile')
    return render(request,'ecom/edit_business_profile.html',context=mydict)
