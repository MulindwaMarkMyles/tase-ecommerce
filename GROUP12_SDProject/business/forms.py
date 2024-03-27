from django import forms
from django.contrib.auth.models import User
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','category','price','description','product_image']

class BusinessUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model=models.Business
        fields=['address','mobile','business_pic']