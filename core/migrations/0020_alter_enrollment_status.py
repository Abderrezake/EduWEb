# Generated by Django 5.0.3 on 2024-05-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_course_level_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('isntStart', 'isntStart'), ('finiched', 'finiched'), ('inProgress', 'inProgress')], default='isntStart', max_length=20),
        ),
    ]
