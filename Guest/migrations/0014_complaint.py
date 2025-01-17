# Generated by Django 5.0 on 2024-04-13 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0013_tbl_queries'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=500)),
                ('complaint_content', models.CharField(max_length=500)),
                ('comaplaint_replay', models.CharField(max_length=500)),
                ('comaplaint_status', models.CharField(max_length=1)),
                ('complaint_date', models.DateField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_coach')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
