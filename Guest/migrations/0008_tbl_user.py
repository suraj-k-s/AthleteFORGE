# Generated by Django 5.0 on 2024-02-19 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_admin'),
        ('Guest', '0007_tbl_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=20)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_gender', models.CharField(max_length=20)),
                ('user_address', models.CharField(max_length=500)),
                ('user_dob', models.CharField(max_length=20)),
                ('user_photo', models.FileField(upload_to='Userphoto/')),
                ('user_proof', models.FileField(upload_to='Userproof/')),
                ('user_password', models.CharField(max_length=20)),
                ('user_vstatus', models.CharField(max_length=20)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
