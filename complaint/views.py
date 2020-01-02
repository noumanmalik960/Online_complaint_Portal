from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm, StatusForm, EditComplaintForm
from django.contrib.auth.decorators import login_required
# for twilio sms service
from twilio.rest import Client



# for email
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'complaint/home.html')

def complaint(request):
    if request.method != 'POST':
        form = ComplaintForm()

    else:
        form = ComplaintForm(data=request.POST)
        if form.is_valid():
            form.save()
            # Send email functionlity
            subject = 'Online Complaint System'
            message = 'Your complaint has been filed succesfully at online complaint portal.'
            email_from = settings.EMAIL_HOST_USER
            send_to = form.cleaned_data['email']
            recipient_list = [send_to]

            send_mail(subject, message, email_from, recipient_list)


            # # sms functionality
            # # Your Account SID from twilio.com/console
            # account_sid = "ACa5f76db99b4487f41591f766088ac12c"
            # # Your Auth Token from twilio.com/console
            # auth_token = "b7b094b45326bad5bbf08856ba82e189"

            # client = Client(account_sid, auth_token)

            # con = form.cleaned_data['phone']
            # contact = '+92'+ con[1:]
            # message = client.messages.create(
            # to=contact,
            # from_="+18603984426",
            # body="Your complaint has been successfully filed. It will take a week or two to entertain your case.")
            # print(message.sid)

            return redirect('complaint:home')

    context = {'form': form}
    return render(request, 'complaint/complaint_form.html', context)


def status(request):
    if request.method != 'POST':
        result = 'None'
        form = StatusForm()

    else:
        form = StatusForm(data=request.POST)
        if form.is_valid():
            nic = form.cleaned_data['nic']
            complaint = get_object_or_404(Complaint, cnic=nic)
            result = complaint

    return render(request, 'complaint/status.html', {'form': form, 'result': result})

# This will need login_required decorators cause only admin can see this
@login_required
def complaint_list(request):
    pen_complaints = Complaint.objects.filter(status='pending')
    ent_complaints = Complaint.objects.filter(status='entertained')

    
    return render(request, 'complaint/complaint_list.html', {'pen_complaints': pen_complaints, 'ent_complaints': ent_complaints})


@login_required
def edit(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    email = complaint.email

    if request.method != 'POST':
        form = EditComplaintForm(instance=complaint)

    else:
        form = EditComplaintForm(instance=complaint, data=request.POST)
        if form.is_valid():
            
            # SEND EMAIL FUNCTIONALITY
            if form.cleaned_data['status'] != 'pending':
                subject = 'Online Complaint System'
                message = 'Your complaint has been successfully updated. You can check your complaint status on the portal.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]

                send_mail(subject, message, email_from, recipient_list)

            form.save()
            return redirect('complaint:complaint_list')

    context = {'complaint': complaint, 'form': form}
    return render(request, 'complaint/edit.html', context)


def about(request):
    return render(request, 'complaint/about.html')
