# Generated by Django 5.0.3 on 2024-05-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_post_zoom_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('isntStart', 'isntStart'), ('inProgress', 'inProgress'), ('finiched', 'finiched')], default='isntStart', max_length=20),
        ),
    ]
