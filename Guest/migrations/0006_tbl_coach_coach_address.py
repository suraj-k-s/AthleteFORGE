# Generated by Django 5.0 on 2024-02-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_coach_coach_vstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_coach',
            name='coach_address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
