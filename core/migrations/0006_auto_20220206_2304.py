# Generated by Django 3.2.11 on 2022-02-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220206_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
