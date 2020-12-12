from django import forms
from django.forms import ModelForm
from templateapp.models import User_infor,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class CreateForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=200)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserInfo(ModelForm):

	class Meta:
		model = User_infor
		fields = ['user_dob','user_weight','user_height','user_gender','user_goal','user_profession','user_lifestyle','user_medicalhistory','user_foodprefer']

