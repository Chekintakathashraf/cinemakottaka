# Generated by Django 4.1.2 on 2022-11-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0010_alter_bokkingticket_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bokkingticket',
            old_name='seet_no',
            new_name='seat_no',
        ),
    ]
