# Generated by Django 5.0.4 on 2024-04-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_found_item_image_lost_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found_item',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='found_item',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]