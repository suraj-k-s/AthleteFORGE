# Generated by Django 5.0 on 2024-03-08 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_admin'),
        ('Guest', '0009_alter_tbl_user_user_vstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_coach',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_event'),
        ),
    ]
