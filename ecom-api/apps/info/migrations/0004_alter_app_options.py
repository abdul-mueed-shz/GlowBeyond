# Generated by Django 4.1.2 on 2023-12-17 21:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("info", "0003_app"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="app",
            options={"verbose_name": "App", "verbose_name_plural": "App"},
        ),
    ]
