# Generated by Django 5.0.6 on 2024-08-16 20:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_guest_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]