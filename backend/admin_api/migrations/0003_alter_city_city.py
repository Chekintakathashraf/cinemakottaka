# Generated by Django 4.1.2 on 2022-10-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0002_alter_district_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]