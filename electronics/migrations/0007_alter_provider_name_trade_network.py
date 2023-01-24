# Generated by Django 4.1.3 on 2023-01-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electronics", "0006_alter_provider_name_trade_network"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="name_trade_network",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[(0, "Завод"), (1, "Розница")],
                null=True,
                verbose_name="Звено цепи",
            ),
        ),
    ]
