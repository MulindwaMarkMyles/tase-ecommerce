from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Business(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    businessname = models.CharField(max_length=40)
    business_pic= models.ImageField(upload_to='profile_pic/BusinessProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name_plural='Businesses'
    
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    business=models.ForeignKey(Business,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40,null=True,blank=True)
    
    def __str__(self):
        return self.name
