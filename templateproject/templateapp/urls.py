from django.urls import path
from .import views
urlpatterns = [
path('', views.homePageView, name ='index'), 
path('signup/',views.signup, name ='signup'),
path('loginpage/',views.loginpage, name ='loginpage'),
path('contact/',views.contact, name ='contact'),
path('about/',views.about, name ='about'),
path('userinfo/',views.userinfo, name ='userinfo'),
path('mealplan/',views.mealplan,name='mealplan'),
path('logoutpage/',views.logout,name='logoutpage'),
path('profile/',views.profile,name='profile'),
path('profile/mealplan',views.mealplan,name='mealplan'),
path('account_setting/',views.account_setting,name='account_setting'),



]

