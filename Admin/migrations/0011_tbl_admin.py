# Generated by Django 5.0 on 2024-02-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=20)),
                ('admin_email', models.CharField(max_length=20)),
                ('admin_password', models.CharField(max_length=20)),
            ],
        ),
    ]
