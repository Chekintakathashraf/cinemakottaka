# Generated by Django 4.1.2 on 2022-11-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0018_alter_brokercharge_brokerfee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokercharge',
            name='brokerfee',
            field=models.FloatField(default=0),
        ),
    ]