from .models import Complaint
from django import forms

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_for', 'name', 'cnic', 'gender', 'address', 'city', 'phone', 'email', 'against', 'complaint_details', 'adressed_to']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'cnic': forms.TextInput(attrs={'placeholder': 'without dashes'}),
            'phone': forms.TextInput(attrs={'placeholder': 'without dash'}),
            'email': forms.TextInput(attrs={'placeholder': 'someone@example.com'}),
            'complaint_details': forms.Textarea(attrs={'placeholder': 'Please limit your text to 1800 characters only'}),
        }

class StatusForm(forms.Form):
    nic = forms.CharField(max_length=13)


class EditComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status']