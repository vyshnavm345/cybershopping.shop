# Generated by Django 4.2.5 on 2023-10-07 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_category_verified"),
    ]

    operations = [
        migrations.CreateModel(
            name="Headphone",
            fields=[
                (
                    "product_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="products.product",
                    ),
                ),
                ("headphone_type", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "headphone",
            },
            bases=("products.product",),
        ),
        migrations.RemoveField(
            model_name="keyboard",
            name="keyboard_type",
        ),
        migrations.RemoveField(
            model_name="monitor",
            name="display_type",
        ),
    ]