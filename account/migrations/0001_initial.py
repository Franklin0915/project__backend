# Generated by Django 4.2.3 on 2023-07-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(default='White', max_length=255)),
                ('plate_number', models.CharField(max_length=255)),
                ('owner_fullname', models.CharField(max_length=255)),
                ('registered_at', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
