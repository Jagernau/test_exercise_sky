# Generated by Django 4.1.3 on 2023-01-24 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("electronics", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="addresscompany",
            options={"verbose_name": "Адресс", "verbose_name_plural": "Адреса"},
        ),
        migrations.AlterModelOptions(
            name="contacts",
            options={"verbose_name": "Контакт", "verbose_name_plural": "Контакты"},
        ),
    ]
