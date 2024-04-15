# Generated by Django 5.0.4 on 2024-04-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0012_found_item_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="found_item",
            name="user",
        ),
        migrations.RemoveField(
            model_name="lost_item",
            name="user",
        ),
        migrations.AddField(
            model_name="found_item",
            name="image_description",
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="lost_item",
            name="image_description",
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
