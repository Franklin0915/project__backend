# Generated by Django 4.2.3 on 2023-09-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredvehicle',
            name='car_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registeredvehicle',
            name='cars_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='registeredvehicle',
            name='drivers_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='registeredvehicle',
            name='numberplate_state',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registeredvehicle',
            name='owner_gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True),
        ),
    ]
