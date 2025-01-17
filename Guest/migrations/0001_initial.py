# Generated by Django 5.0 on 2024-02-03 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_tbl_scategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_name', models.CharField(max_length=20)),
                ('coach_email', models.CharField(max_length=20)),
                ('coach_contact', models.CharField(max_length=20)),
                ('coach_gender', models.CharField(max_length=20)),
                ('coach_dob', models.CharField(max_length=20)),
                ('coach_photo', models.FileField(upload_to='CoachDoc/')),
                ('coach_licence', models.FileField(upload_to='Coachlic')),
                ('coach_password', models.CharField(max_length=20)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
