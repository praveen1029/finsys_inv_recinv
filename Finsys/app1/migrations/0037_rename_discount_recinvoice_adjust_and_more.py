# Generated by Django 4.2.3 on 2023-11-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0036_recinvoice_tot_inv_no"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recinvoice", old_name="discount", new_name="adjust",
        ),
        migrations.RemoveField(model_name="recinvoice", name="gsttype",),
        migrations.AddField(
            model_name="recinvoice",
            name="balance",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="bank_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="cheque_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="paidoff",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="pay_method",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="shipping_charge",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="recinvoice",
            name="upi_no",
            field=models.CharField(default="", max_length=255, null=True),
        ),
    ]
