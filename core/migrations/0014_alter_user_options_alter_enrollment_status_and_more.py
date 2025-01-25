# Generated by Django 5.0.4 on 2024-05-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_add_course', 'Can add courses'), ('can_delete_course', 'Can delete courses'), ('can_add_video', 'Can add videos'), ('can_delete_video', 'Can delete videos'), ('can_manage_credit', 'Can manage student credit')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('inProgress', 'inProgress'), ('finiched', 'finiched'), ('isntStart', 'isntStart')], default='isntStart', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='zoom_link',
            field=models.URLField(default='', max_length=100),
        ),
    ]
