# Generated by Django 3.1.3 on 2020-11-19 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_employee_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
