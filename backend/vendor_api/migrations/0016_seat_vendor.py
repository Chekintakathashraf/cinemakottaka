# Generated by Django 4.1.2 on 2022-10-26 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_api', '0015_seat_booked_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_api.vendor'),
        ),
    ]
