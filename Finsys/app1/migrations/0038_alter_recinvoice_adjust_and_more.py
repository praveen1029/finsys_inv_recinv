# Generated by Django 4.2.3 on 2023-11-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0037_rename_discount_recinvoice_adjust_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recinvoice",
            name="adjust",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="recinvoice",
            name="shipping_charge",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="recinvoice",
            name="taxamount",
            field=models.FloatField(default=0, null=True),
        ),
    ]
