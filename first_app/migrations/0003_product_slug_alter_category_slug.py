# Generated by Django 5.1.4 on 2024-12-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0002_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="", max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
