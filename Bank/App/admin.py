from django.contrib import admin

from .models import TrustCall, Users, Message, Contact, Loan, Staff, Payment

# Register your models here.

admin.site.register(TrustCall)
admin.site.register(Users)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Loan)
admin.site.register(Staff)
admin.site.register(Payment)
