# Generated by Django 5.0.3 on 2024-04-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('finiched', ''), ('inProgress', ''), ('isntStart', '')], default='isntStart', max_length=20),
        ),
    ]
