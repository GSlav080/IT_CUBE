# Generated by Django 4.1.4 on 2023-01-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="information",
            name="N",
            field=models.CharField(
                default=1, max_length=2, verbose_name="НОмер кабинета"
            ),
            preserve_default=False,
        ),
    ]