# Generated by Django 5.0 on 2024-04-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_tbl_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_subscribe',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
