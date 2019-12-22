from django.db import models
from django.utils import timezone

# Create your models here.


class Complaint(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('entertained', 'Entertained'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('trans', 'Trans'),
    )
    COMPLAINT_CHOICES = (
        ('misbehave', 'Misbehave'),
        ('illegal gratification', 'Illegal Gratification'),
        ('faulty investigation', 'Faulty Investigation'),
        ('manhandling', 'Manhandling'),
        ('non registration of cases', 'Non registration of cases'),
        ('traffic', 'Traffic'),
        ('other', 'Other')
    )
    AGAINST_CHOICES = (
        ('public', 'Public'),
        ('police', 'Police'),
    )
    ADRESSED_TO_CHOICES = (
        ('IGP', 'IGP'),
        ('DIG OPS', 'DIG OPS'),
        ('other', 'OTHER'),
    )
    CITY_CHOICES = (
        ('islamabad', 'Islamabad'),
        ('lahore', 'Lahore'),
        ('peshawar', 'Peshawar'),
        ('karachi', 'Karachi'),
        ('other', 'Other'),
    )
    complaint_for = models.CharField(max_length=25, choices=COMPLAINT_CHOICES, default='Misbehave')
    name = models.CharField(max_length=50)
    cnic = models.CharField(verbose_name='CNIC', max_length=13, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Trans')
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=20, choices=CITY_CHOICES , default='Islamabad')
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    against = models.CharField(max_length=10, choices=AGAINST_CHOICES, default='Public')
    complaint_details = models.TextField(max_length=1800)
    adressed_to = models.CharField(max_length=15, choices=ADRESSED_TO_CHOICES, default='IGP')
    
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='pending')



    class Meta:
        ordering = ('-status',)

    def __str__(self):
        return self.complaint_for.title()