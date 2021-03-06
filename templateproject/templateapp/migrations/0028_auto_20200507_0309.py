# Generated by Django 3.0.4 on 2020-05-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateapp', '0027_auto_20200507_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_infor',
            name='user_dob',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_foodprefer',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-veg'), ('Veg(with eggs)', 'Veg(with eggs)')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_goal',
            field=models.CharField(choices=[('Muscle building', 'Muscle building'), ('Fat loss', 'Fat loss')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_lifestyle',
            field=models.CharField(choices=[('Sedentary', 'Sedentary'), ('Lightly active', 'Lightly active'), ('Moderately active', 'Moderately active'), ('Very active', 'Very active'), ('Extremely active', 'Extremely active')], max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_medicalhistory',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_profession',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_infor',
            name='user_weight',
            field=models.FloatField(),
        ),
    ]
