# Generated by Django 4.1.2 on 2023-12-07 19:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_product_price"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="category",
            table="category",
        ),
        migrations.AlterModelTable(
            name="product",
            table="product",
        ),
    ]
