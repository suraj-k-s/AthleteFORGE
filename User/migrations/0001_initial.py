# Generated by Django 5.0 on 2024-02-20 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0009_alter_tbl_user_user_vstatus'),
        ('Shop', '0004_rename_product_id_tbl_product_gallery_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.CharField(max_length=20)),
                ('booking_deliverydate', models.CharField(max_length=20)),
                ('booking_amount', models.CharField(max_length=20)),
                ('booking_status', models.CharField(default='0', max_length=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_quantity', models.CharField(max_length=10)),
                ('cart_status', models.CharField(default='0', max_length=1, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
            ],
        ),
    ]
