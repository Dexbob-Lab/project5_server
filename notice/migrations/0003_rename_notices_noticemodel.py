# Generated by Django 5.1.2 on 2024-10-30 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0002_alter_notices_view_count"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Notices",
            new_name="NoticeModel",
        ),
    ]