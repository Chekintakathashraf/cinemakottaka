# Generated by Django 4.1.2 on 2022-11-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0009_remove_bokkingticket_ticket_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokkingticket',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
