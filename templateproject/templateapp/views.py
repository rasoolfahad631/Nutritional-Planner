from django.shortcuts import render,redirect,get_object_or_404
from templateapp.models import User_infor,Customer
from django.contrib import messages
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.models import Group




# Create your views here.
from .forms import  CreateForm,UserInfo,CustomerForm



def loginpage(request):
			if request.method == 'POST':                                                           
				username=request.POST.get("username")
				password=request.POST.get("password")
				user = authenticate(request, username=username, password=password)
				if user is not None:
					login(request, user)
					return redirect('profile')
				else:
					messages.info(request, 'Username OR password is incorrect')
			context = {}
			return render(request,"templateapp/loginpage.html",context)

def contact(request):
	return render(request,"templateapp/contact.html")

def about(request):
	return render(request,"templateapp/about.html")

def profile(request):
	info = User_infor.objects.get(user=request.user)
	if info.user_gender == 'Male':
		BMR = 10 * float(info.user_weight) + 6.25 * float(info.user_height) - 5 * int(info.user_dob) + 5
	else:
		BMR = 10 * float(info.user_weight) + 6.25 * float(info.user_height) - 5 * int(info.user_dob) - 161
	if info.user_lifestyle == 'Sedentary':
		calories = BMR * 1.2
	if info.user_lifestyle == 'Lightly active':
		calories = BMR * 1.375
	if info.user_lifestyle == 'Moderately active':
		calories = BMR * 1.55
	if info.user_lifestyle == 'Very active':
		calories = BMR * 1.725
	if info.user_lifestyle == 'Extremely active':
		calories = BMR * 1.9
	context ={'info':info,'BMR':BMR,'calories':calories}
	return render(request,"templateapp/profile.html",context)

def account_setting(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'templateapp/account_setting.html', context)



	
def userinfo(request):
	f = UserInfo()
	if request.method == 'POST':
		f = UserInfo(request.POST)
		if f.is_valid():
			pr = User_infor()
			pr.user = User.objects.get(id=request.user.id)
			pr.user_dob = f.cleaned_data['user_dob']
			pr.user_weight = f.cleaned_data['user_weight']
			pr.user_height = f.cleaned_data['user_height']
			pr.user_gender = f.cleaned_data['user_gender']
			pr.user_goal = f.cleaned_data['user_goal']
			pr.user_profession = f.cleaned_data['user_profession']
			pr.user_lifestyle = f.cleaned_data['user_lifestyle']
			pr.user_medicalhistory = f.cleaned_data['user_medicalhistory']
			pr.user_foodprefer = f.cleaned_data['user_foodprefer']
			pr.save()
			messages.success(request, f'Form has been submitted  successfully')
			return redirect('loginpage')
		else:
		    messages.error(request, AssertionError)
	else:
		f = UserInfo()
	return render(request, "templateapp/userinfo.html", context={'f': f})



def homePageView(request):
	return render(request,"templateapp/homepage.html")

def signup(request):	
	form = CreateForm()
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				name=user.username,
				useremail=user.email,
			
				)
			login(request, user)
			


			return redirect('userinfo')
	context ={'form':form,}
	return render(request, 'templateapp/signup.html',context)

def mealplan(request):
	return render(request, 'templateapp/mealplan.html',)



def logoutpage(request):
	logout(request)
	return redirect('loginpage')


