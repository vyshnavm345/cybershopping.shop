# Generated by Django 4.2.5 on 2023-10-17 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0026_address_name_cart_quantity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitems",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="orderitems",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="products.product"
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]