# Generated by Django 4.1.13 on 2024-07-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TokiyoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddressdetail',
            name='customerDeliveryNumber',
            field=models.CharField(max_length=15, verbose_name='Delivery Phone No'),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='customerPhone',
            field=models.CharField(max_length=15, verbose_name='Phone No'),
        ),
    ]
