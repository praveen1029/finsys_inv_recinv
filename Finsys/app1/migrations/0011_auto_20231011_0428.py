# Generated by Django 3.2.22 on 2023-10-11 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20231011_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='stock_rate',
            field=models.FloatField(blank=True, default='0.0', null=True),
        ),
        migrations.CreateModel(
            name='holidays',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False, verbose_name='hid')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('atid', models.AutoField(primary_key=True, serialize=False, verbose_name='hid')),
                ('date', models.DateField(blank=True, null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
