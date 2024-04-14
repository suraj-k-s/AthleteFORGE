# Generated by Django 5.0 on 2024-04-06 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_tbl_coach_event'),
        ('User', '0004_tbl_shopcomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_review', models.IntegerField()),
                ('rating_data', models.CharField(max_length=50)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_coach')),
            ],
        ),
    ]