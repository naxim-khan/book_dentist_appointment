# Generated by Django 5.0 on 2024-04-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0003_appointment_alter_dentistregistration_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dentistregistration',
            name='password',
        ),
    ]