# Generated by Django 5.0 on 2024-02-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_booking',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbl_booking',
            name='booking_deliverydate',
            field=models.DateField(),
        ),
    ]