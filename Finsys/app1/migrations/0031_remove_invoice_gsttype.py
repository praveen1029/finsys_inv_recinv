# Generated by Django 4.2.3 on 2023-11-02 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0030_invoice_cheque_no_invoice_pay_method_invoice_upi_no"),
    ]

    operations = [
        migrations.RemoveField(model_name="invoice", name="gsttype",),
    ]