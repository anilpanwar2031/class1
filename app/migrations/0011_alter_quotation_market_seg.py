# Generated by Django 4.1.4 on 2022-12-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_quotation_quot_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='market_seg',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
