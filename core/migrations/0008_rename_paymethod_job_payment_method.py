# Generated by Django 3.2.11 on 2022-02-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_job_paymethod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='paymethod',
            new_name='payment_method',
        ),
    ]
