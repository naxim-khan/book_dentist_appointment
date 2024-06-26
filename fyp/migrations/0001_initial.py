# Generated by Django 5.0 on 2024-03-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DentistRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('specialization', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(max_length=128)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
