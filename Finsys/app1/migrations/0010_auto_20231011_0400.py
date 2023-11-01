# Generated by Django 3.2.22 on 2023-10-11 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_e_waybill_item_e_waybills_transportation'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedebit',
            name='amtrecvd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='balance_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='balance_due',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='discount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='paid_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='payment_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='round_off',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='ship_charge',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Save', 'Save')], default='Draft', max_length=150),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='tcs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='tcs_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='total_discount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit1',
            name='discount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='debitnotecomments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('debid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
            ],
        ),
    ]
