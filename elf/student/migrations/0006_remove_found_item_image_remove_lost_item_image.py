# Generated by Django 5.0.4 on 2024-04-06 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_found_item_date_alter_lost_item_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found_item',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lost_item',
            name='image',
        ),
    ]