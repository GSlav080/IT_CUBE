# Generated by Django 4.1.4 on 2023-01-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_information_n"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="N",
            field=models.CharField(max_length=2, verbose_name="Номер кабинета"),
        ),
    ]