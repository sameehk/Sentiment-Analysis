"""sentiment_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from sentimentapp import views

urlpatterns = [
    path('',views.userlogin),
    path('usercomplaint1',views.usercomplaint1),
    path('regdetails',views.regdetails),
    path('feedback',views.feedback),
    path('usercomplaint2',views.usercomplaint2),
    path('userfeedback',views.userfeedback),
    path('register',views.register),
    path('userhome',views.userhome),
    path('complaint',views.complaint),
    path('complaintreply',views.complaintreply),
    path('searchuser',views.searchuser),
    path('usercompsearch',views.usercompsearch),

    path('adminfeedback',views.adminfeedback),
    path('Admin_userdetails',views.adminuserdetails),
    path('blockuser/<int:id>',views.blockuser),
    path('unblockuser/<int:id>',views.unblockuser),
    path('admincomplaint',views.admincomplaint),
    path('searchdate',views.searchdate),
    path('feedbacksearchdate',views.feedbacksearchdate),
    path('admincomplaintreply/<int:id>',views.admincomplaintreply),
    path('admincomplaint',views.adminfeedback),
    path('adminhome',views.adminhome),
    path('adminhome',views.adminhome),
    path('loginpost',views.loginpost),
    path('insert_review',views.insert_review),



]

