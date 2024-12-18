# Generated by Django 5.1.4 on 2024-12-12 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0005_alter_product_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="SomeEntity",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="one_to_one",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="one_to_one",
                to="first_app.someentity",
            ),
        ),
    ]
