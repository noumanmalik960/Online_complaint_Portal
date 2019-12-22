# Generated by Django 2.2.7 on 2019-12-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0009_auto_20191206_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='adressed_to',
            field=models.CharField(choices=[('IGP', 'IGP'), ('DIG OPS', 'DIG OPS'), ('other', 'OTHER')], default='IGP', max_length=15),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='body',
            field=models.TextField(max_length=1800),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='cnic',
            field=models.CharField(max_length=13, verbose_name='CNIC'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]