# Generated by Django 4.1.2 on 2022-11-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0015_remove_movie_name'),
        ('user_api', '0005_usertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_api.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_api.district'),
        ),
    ]
