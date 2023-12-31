"""Expense_Tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from ExpenseTracker import views
from ExpenseTracker import Dashboardview
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/landingpage',views.LandingPage),
    re_path(r'^api/submitexpensepage',views.Expensepage),
    re_path(r'^api/submitexpense',views.SubmitExpense),
    re_path(r'^api/dashboard',views.Dashboard),
    re_path(r'^api/filldata',views.Filldata),
    re_path(r'^api/userdataindb',views.Userdata),
    re_path(r'^api/checkuserlogin',views.CheckUserLogin),
    re_path(r'^api/session',views.session),
    re_path(r'^api/editentry',views.EditDelete),
    
    # re_path(r'^api/editdeleterecord',Dashboardview.),


]
