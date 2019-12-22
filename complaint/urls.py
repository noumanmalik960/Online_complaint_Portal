from django.urls import path
from .models import Complaint
from . import views

app_name = 'complaint'

urlpatterns = [
    # complaint views

    path('', views.home, name='home'),
    
    # Complaint form
    path('complaint/', views.complaint, name='complaint'),

    # For about
    path('about/', views.about, name='about'),

    # For complaint status
    path('status/', views.status, name='status'),

    # for admin to see and edit the status of complaints
    path('complaint_list/', views.complaint_list, name='complaint_list'),

    # Edit option for admin to edit the status
    path('edit/<int:complaint_id>/', views.edit, name='edit'),
]