# Generated by Django 5.0.3 on 2025-01-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('inProgress', 'inProgress'), ('finiched', 'finiched'), ('isntStart', 'isntStart')], default='isntStart', max_length=20),
        ),
    ]
