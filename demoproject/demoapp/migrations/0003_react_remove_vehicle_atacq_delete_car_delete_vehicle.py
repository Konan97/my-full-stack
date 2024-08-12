# Generated by Django 5.0.7 on 2024-07-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demoapp", "0002_remove_car_type_car_atacq_item_car_rfid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="React",
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
                ("user", models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="ATACQ",
        ),
        migrations.DeleteModel(
            name="Car",
        ),
        migrations.DeleteModel(
            name="Vehicle",
        ),
    ]
