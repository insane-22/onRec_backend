# Generated by Django 5.0.6 on 2024-07-07 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_date_uploaded_podcast_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='podcast',
            name='name',
            field=models.ForeignKey(default='onrec', on_delete=django.db.models.deletion.CASCADE, to='api.guest'),
            preserve_default=False,
        ),
    ]
