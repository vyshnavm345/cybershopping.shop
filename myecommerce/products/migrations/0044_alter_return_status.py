# Generated by Django 4.2.5 on 2023-10-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0043_alter_return_status"),
    ]

    operations = [
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