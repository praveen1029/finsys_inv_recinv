# Generated by Django 4.2.3 on 2023-11-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0027_invoice_ref_no"),
    ]

    operations = [
        migrations.RemoveField(model_name="invoice", name="ref_no",),
    ]