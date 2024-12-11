# Generated by Django 5.1.4 on 2024-12-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0004_producttag_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="first_app.producttag"
            ),
        ),
    ]
