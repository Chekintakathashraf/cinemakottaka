# Generated by Django 4.1.2 on 2022-11-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0020_alter_brokercharge_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokercharge',
            name='payment_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
