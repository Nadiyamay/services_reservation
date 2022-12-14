# Generated by Django 4.1.2 on 2022-10-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_services', models.CharField(help_text='Enter the name of service', max_length=20)),
                ('service_place', models.CharField(help_text='Select service place', max_length=20)),
                ('client_name', models.CharField(help_text='Enter client name', max_length=35)),
                ('client_email', models.EmailField(help_text='Enter client email', max_length=254)),
                ('client_date_of_birth', models.DateField(help_text="Enter client's birth day")),
                ('client_point_of_service', models.IntegerField(help_text="Enter client's point")),
                ('comment', models.TextField(max_length=250)),
            ],
            options={
                'ordering': ['-name_of_services'],
            },
        ),
    ]
