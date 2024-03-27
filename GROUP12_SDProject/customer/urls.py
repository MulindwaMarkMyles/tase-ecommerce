"""



"""

from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',home_view,name=''),
    path('afterlogin/', afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='customer/logout.html'),name='logout'),
    path('aboutus/', aboutus_view),
    path('contactus/', contactus_view,name='contactus'),
    path('search/', search_view,name='search'),
    path('send-feedback/', send_feedback_view,name='send-feedback'),
    path('customersignup/', customer_signup_view),
    path('customerlogin/', LoginView.as_view(template_name='customer/customerlogin.html'),name='customerlogin'),
    path('customersignup/customerlogin/', LoginView.as_view(template_name='customer/customerlogin.html'),name='customerlogin'),
    path('customer-home/', customer_home_view,name='customer-home'),
    path('product_detail/<int:pk>', product_detail,name='product-detail'),
    path('my-order/', my_order_view,name='my-order'),
    path('my-profile/', my_profile_view,name='my-profile'),
    path('edit-profile/', edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', download_invoice_view,name='download-invoice'),
    path('add-to-cart/<int:pk>', add_to_cart_view,name='add-to-cart'),
    path('cart/', cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart_view,name='remove-from-cart'),
    path('customer-address/', customer_address_view,name='customer-address'),
    path('payment-success/', payment_success_view,name='payment-success'),
]
