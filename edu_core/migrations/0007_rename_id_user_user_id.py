# Generated by Django 4.2.16 on 2024-12-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edu_core", "0006_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="id",
            new_name="user_id",
        ),
    ]
