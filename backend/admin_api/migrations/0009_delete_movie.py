# Generated by Django 4.1.2 on 2022-10-21 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0008_movie_dateofadd_alter_movie_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
