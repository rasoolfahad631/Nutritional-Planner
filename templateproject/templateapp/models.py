from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
Gender = (
            ('MALE','Male'),
            ('FEMALE','Female'),
            )

Goal = (
            ('Muscle building','Muscle building'),
            ('Fat loss','Fat loss'),
            )

lifestyle = (
            ('Sedentary','Sedentary'),
            ('Lightly active','Lightly active'),
			('Moderately active','Moderately active'),
			('Very active','Very active'),
			('Extremely active','Extremely active'),
            )

foodprefer = (
            ('Veg','Veg'),
            ('Non-Veg','Non-veg'),
            ('Veg(with eggs)','Veg(with eggs)'),
            )

class Customer(models.Model):
	user = models.OneToOneField(User, null=True,blank = True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	useremail = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name


class User_infor(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	user_dob=models.CharField(max_length=30,)
	user_weight=models.FloatField(blank=False)
	user_height=models.FloatField(blank=False)
	user_gender=models.CharField(choices=Gender,max_length=30,)
	user_goal=models.CharField(choices=Goal,max_length=30,)
	user_profession=models.CharField(max_length=30,)
	user_lifestyle=models.CharField(choices=lifestyle,max_length=30,)
	user_medicalhistory=models.CharField(max_length=30,)
	user_foodprefer=models.CharField(choices=foodprefer,max_length=30)
	def __str__(self):
		return str(self.user)



