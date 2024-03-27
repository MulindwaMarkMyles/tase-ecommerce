from django.contrib import admin
from .models import Customer,Orders,Feedback


class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)


