# Generated by Django 4.2.3 on 2023-11-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0029_invoice_tot_inv_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="cheque_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="pay_method",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="upi_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
    ]
