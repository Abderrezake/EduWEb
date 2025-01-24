# Generated by Django 5.0.3 on 2024-04-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('isntStart', 'isntStart'), ('finiched', 'finiched'), ('inProgress', 'inProgress')], default='isntStart', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
