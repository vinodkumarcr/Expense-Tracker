# Generated by Django 2.0.2 on 2018-10-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0003_auto_20181008_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
