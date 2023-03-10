# Generated by Django 4.1.3 on 2023-01-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AddressCompany",
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
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Страна"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Улица"
                    ),
                ),
                (
                    "house_number",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Номер дома"
                    ),
                ),
            ],
            options={
                "verbose_name": "Адресс",
                "verbose_name_plural": "Адресаы",
            },
        ),
        migrations.CreateModel(
            name="Contacts",
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
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=100, null=True, verbose_name="Почта"
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контактыы",
            },
        ),
        migrations.CreateModel(
            name="Products",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Модель"
                    ),
                ),
                (
                    "launch_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата выпуска"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="Provider",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("debt", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name_trade_network",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[(0, "Завод"), (1, "Розница")],
                        null=True,
                        verbose_name="Звено цепи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
    ]
