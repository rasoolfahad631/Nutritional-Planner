# Generated by Django 3.0.4 on 2020-05-05 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0012_remove_user_infor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_infor',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='templateapp.Customer'),
        ),
    ]