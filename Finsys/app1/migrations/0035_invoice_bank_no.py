# Generated by Django 4.2.3 on 2023-11-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0034_invoice_adjust"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="bank_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
    ]