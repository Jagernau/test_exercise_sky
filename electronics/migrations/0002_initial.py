# Generated by Django 4.1.3 on 2023-01-24 01:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("electronics", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Stuff",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("users.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="TradingNetwork",
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
                        choices=[(1, "Розница"), (2, "Предприниматель")],
                        null=True,
                        verbose_name="Звено цепи",
                    ),
                ),
                (
                    "contacts",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electronics.contacts",
                        verbose_name="Контакты",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electronics.products",
                        verbose_name="Продукция",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="electronics.provider",
                        verbose_name="Поставщик",
                    ),
                ),
                (
                    "stuff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Работники",
                    ),
                ),
            ],
            options={
                "verbose_name": "Покупатель",
                "verbose_name_plural": "Покупатели",
            },
        ),
        migrations.AddField(
            model_name="provider",
            name="contacts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="electronics.contacts",
                verbose_name="Контакты",
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="electronics.products",
                verbose_name="Продукция",
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="stuff",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="electronics.stuff",
                verbose_name="Работники",
            ),
        ),
        migrations.AddField(
            model_name="contacts",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="electronics.addresscompany",
                verbose_name="Адрес",
            ),
        ),
    ]
