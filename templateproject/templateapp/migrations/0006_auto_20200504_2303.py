# Generated by Django 3.0.4 on 2020-05-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0005_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_infor',
            name='user_dob',
            field=models.FloatField(default=None),
        ),
    ]