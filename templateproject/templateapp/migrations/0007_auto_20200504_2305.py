# Generated by Django 3.0.4 on 2020-05-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0006_auto_20200504_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_infor',
            name='user_dob',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
