# Generated by Django 5.0 on 2024-02-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_remove_tbl_place_district_delete_tbl_district'),
        ('Guest', '0003_alter_tbl_coach_place'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_place',
        ),
    ]
