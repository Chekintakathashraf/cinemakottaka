# Generated by Django 4.1.2 on 2022-10-25 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0014_movie_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
    ]
