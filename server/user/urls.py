#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/12/20
# @Filename       : urls.py
# @Desc           :


from django.urls import path

from user import views

urlpatterns = [
    path('getUserData', views.UserView.as_view()),
    path('updateUserData',views.UserView.as_view()),
    path('createUser',views.UserView.as_view()),
    path('isExist',views.isExist)
]