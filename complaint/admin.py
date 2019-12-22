from django.contrib import admin
from .models import Complaint

# Register your models here.
# admin.site.register(Complaint)


@admin.register(Complaint)
class Complaint(admin.ModelAdmin):
    list_display = ('complaint_for', 'name', 'cnic', 'email', 'phone', 'status', 'created')