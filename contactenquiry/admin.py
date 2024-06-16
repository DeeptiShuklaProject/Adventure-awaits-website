from django.contrib import admin
from contactenquiry.models import contactEnquiry
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(contactEnquiry,ContactEnquiryAdmin)
# Register your models here.
