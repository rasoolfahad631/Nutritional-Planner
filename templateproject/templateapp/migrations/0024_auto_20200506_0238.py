# Generated by Django 3.0.4 on 2020-05-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0023_auto_20200506_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_infor',
            name='user_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=30),
        ),
    ]
