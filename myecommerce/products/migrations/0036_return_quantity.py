# Generated by Django 4.2.5 on 2023-10-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0035_return"),
    ]

    operations = [
        migrations.AddField(
            model_name="return",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]