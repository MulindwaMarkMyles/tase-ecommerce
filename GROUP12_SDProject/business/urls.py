
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    # path('afterlogin/', afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='customer/logout.html'),name='logout'),


    path('business-view-feedback/', business_view_feedback_view,name='business-view-feedback'),

    path('adminclick/', adminclick_view),
    path('business-login/', LoginView.as_view(template_name='business/businesslogin.html'),name='businesslogin'),
    path('business-signup/', business_signup_view),
    path('business-signup/businesslogin/', LoginView.as_view(template_name='business/businesslogin.html'),name='businesslogin'),
    # path('adminclick/business-login/', LoginView.as_view(template_name='business/businesslogin.html'),name='businesslogin'),
    path('business-dashboard/', business_dashboard_view,name='business-dashboard'),

    path('business-view-customer/',business_view_customer_view,name='business-view-customer'),
    path('business-delete-customer/<int:pk>', business_delete_customer_view,name='business-delete-customer'),
    path('business-update-customer/<int:pk>', business_update_customer_view,name='business-update-customer'),

    path('business-products/', business_products_view,name='business-products'),
    path('business-add-product/', business_add_product_view,name='business-add-product'),
    path('business-add-product/business-products/', business_products_view,name='business-products'),
    path('delete-product/<int:pk>', business_delete_product_view,name='business-delete-product'),
    path('update-product/<int:pk>', business_update_product_view,name='business-update-product'),

    path('business-view-booking/',business_view_booking_view,name='business-view-booking'),
    path('business-delete-order/<int:pk>', business_delete_order_view,name='business-delete-order'),
    path('business-update-order/<int:pk>', business_update_order_view,name='business-update-order'),
]
