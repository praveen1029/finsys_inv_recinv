# Generated by Django 4.2.3 on 2023-11-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0033_alter_invoice_duedate"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="adjust",
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]