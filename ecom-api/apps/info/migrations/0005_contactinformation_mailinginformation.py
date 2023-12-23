# Generated by Django 4.1.2 on 2023-12-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("info", "0004_alter_app_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isActive", models.BooleanField(default=True)),
                ("isDeleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("info", models.CharField(max_length=1000)),
            ],
            options={
                "verbose_name": "Contact Information",
                "verbose_name_plural": "Contact Informations",
                "db_table": "contact_information",
            },
        ),
        migrations.CreateModel(
            name="MailingInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isActive", models.BooleanField(default=True)),
                ("isDeleted", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("info", models.CharField(max_length=1000)),
            ],
            options={
                "verbose_name": "Mailing Information",
                "verbose_name_plural": "Mailing Informations",
                "db_table": "mailing_information",
            },
        ),
    ]