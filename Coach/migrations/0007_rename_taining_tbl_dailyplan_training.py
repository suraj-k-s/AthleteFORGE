# Generated by Django 5.0 on 2024-03-16 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0006_rename_dailyplan_day_tbl_dailyplan_dailyplan_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_dailyplan',
            old_name='taining',
            new_name='training',
        ),
    ]
