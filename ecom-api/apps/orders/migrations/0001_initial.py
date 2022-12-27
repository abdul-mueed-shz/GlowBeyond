# Generated by Django 4.1.2 on 2022-12-10 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('phone', models.PositiveIntegerField(max_length=15)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('zip_code', models.PositiveIntegerField(max_length=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stripe_token', models.CharField(max_length=250)),
                ('products', models.ManyToManyField(to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]