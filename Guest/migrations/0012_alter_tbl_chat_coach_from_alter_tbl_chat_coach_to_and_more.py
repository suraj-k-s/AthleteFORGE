# Generated by Django 5.0 on 2024-04-06 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0011_tbl_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_chat',
            name='coach_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_from', to='Guest.tbl_coach'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='coach_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_to', to='Guest.tbl_coach'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='user_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='Guest.tbl_user'),
        ),
        migrations.AlterField(
            model_name='tbl_chat',
            name='user_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='Guest.tbl_user'),
        ),
    ]
