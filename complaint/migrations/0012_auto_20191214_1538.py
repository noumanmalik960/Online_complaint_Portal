# Generated by Django 2.2.7 on 2019-12-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0011_auto_20191206_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_for',
            field=models.CharField(choices=[('misbehave', 'Misbehave'), ('illegal gratification', 'Illegal Gratification'), ('faulty investigation', 'Faulty Investigation'), ('manhandling', 'Manhandling'), ('non registration of cases', 'Non registration of cases'), ('traffic', 'Traffic'), ('other', 'Other')], default='Misbehave', max_length=25),
        ),
    ]