# Generated by Django 5.0.4 on 2024-04-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_lost_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='found_item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]