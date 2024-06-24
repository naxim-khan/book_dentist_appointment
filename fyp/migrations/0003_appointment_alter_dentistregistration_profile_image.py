# Generated by Django 5.0 on 2024-04-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0002_dentistregistration_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_email', models.EmailField(max_length=254)),
                ('patient_mobile', models.CharField(max_length=15)),
                ('dentist', models.CharField(max_length=100)),
                ('appointment_date', models.DateField()),
                ('problem_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='dentistregistration',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
