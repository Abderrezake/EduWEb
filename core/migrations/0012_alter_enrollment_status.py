# Generated by Django 5.0.3 on 2024-05-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('finiched', 'finiched'), ('inProgress', 'inProgress'), ('isntStart', 'isntStart')], default='isntStart', max_length=20),
        ),
    ]
