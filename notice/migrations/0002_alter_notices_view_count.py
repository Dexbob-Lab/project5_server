# Generated by Django 5.1.2 on 2024-10-30 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notices",
            name="view_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]