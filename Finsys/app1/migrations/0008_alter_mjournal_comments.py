# Generated by Django 3.2.22 on 2023-10-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_mjournal_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mjournal',
            name='comments',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
