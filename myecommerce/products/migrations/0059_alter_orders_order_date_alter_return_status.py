# Generated by Django 4.2.3 on 2023-11-15 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0058_alter_orders_order_date_alter_return_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="order_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 15, 14, 59, 21, 949585, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="return",
            name="status",
            field=models.CharField(
                choices=[("Confirmed", "Confirmed"), ("Pending", "Pending")],
                default="Pending",
                max_length=20,
            ),
        ),
    ]