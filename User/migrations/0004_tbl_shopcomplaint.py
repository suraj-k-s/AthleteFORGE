# Generated by Django 5.0 on 2024-03-16 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_tbl_coach_event'),
        ('User', '0003_alter_tbl_booking_booking_deliverydate'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_shopcomplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopcompliant_title', models.CharField(max_length=100)),
                ('shopcomplaint_content', models.CharField(max_length=500)),
                ('shopcomplaint_reply', models.CharField(max_length=500)),
                ('shopcomplaint_status', models.CharField(default='0', max_length=1)),
                ('shopcomplaint_date', models.DateField(auto_now_add=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]