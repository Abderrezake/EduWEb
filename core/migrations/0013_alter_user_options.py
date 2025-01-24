# Generated by Django 5.0.3 on 2024-05-02 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_add_course', 'Can add courses'), ('can_delete_course', 'Can delete courses'), ('can_add_video', 'Can add videos'), ('can_delete_video', 'Can delete videos'), ('can_manage_credit', 'Can manage student credit'), ('can_add_post', 'Can ...')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
