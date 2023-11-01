# Generated by Django 3.2.22 on 2023-10-12 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_man_journal_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.TextField(max_length=100)),
                ('account_number', models.TextField(max_length=100)),
                ('lenderbank', models.TextField(max_length=100)),
                ('recieced_bank', models.TextField(max_length=100)),
                ('intrest', models.TextField(max_length=100)),
                ('term', models.TextField(max_length=100)),
                ('loan_amount', models.TextField(max_length=100)),
                ('processing', models.TextField(max_length=100)),
                ('paid', models.TextField(max_length=100)),
                ('status', models.TextField(max_length=100)),
                ('desc', models.TextField(max_length=100)),
                ('balance', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, null=True)),
                ('recieved_amount', models.IntegerField(default=0)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.AlterField(
            model_name='recinvoice',
            name='startdate',
            field=models.DateField(default=''),
        ),
        migrations.CreateModel(
            name='loan_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_type', models.TextField(max_length=100)),
                ('from_trans', models.TextField(max_length=100)),
                ('to_trans', models.TextField(max_length=100)),
                ('loan_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('loan_desc', models.TextField(blank=True, null=True)),
                ('loan_date', models.DateField(blank=True, null=True)),
                ('loan_intrest', models.TextField(default=0, max_length=100)),
                ('balance', models.IntegerField(default=0)),
                ('type', models.TextField(max_length=100)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.loan_account')),
            ],
        ),
    ]