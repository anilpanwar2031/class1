# Generated by Django 4.1.4 on 2022-12-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_quotation_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='created_by',
            field=models.CharField(default='a@gmail.com', max_length=200),
        ),
    ]
