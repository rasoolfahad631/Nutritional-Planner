# Generated by Django 3.0.4 on 2020-05-08 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0031_auto_20200508_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='profile_pi',
            new_name='profile_pic',
        ),
    ]