from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from chats import *
app_name = "accounts"
urlpatterns=[
    path('',views.index,name="Login"),
    path('logins',views.logins,name="logins"),
    path('register',views.register,name="register"),
    path('registers',views.registers,name="registers"),
    path('profile',views.profile,name="profile"),
    path('home',login_required(views.home),name="home"),
    path('post',login_required(views.post),name="post"),
    path("friendsf/",views.friendsf,name="friendsf"),
    path("upprof",views.upprof,name="upprof"),
    path("updatebio",views.updatebio,name="updatebio"),
    path("logout",views.logouts,name="logout"),
    path("forgot",views.forgot,name="forgot"),
    path("/<str:user_name>",views.findf,name='ff'),
    
    path("<str:user_name>/follow",views.follow,name="follow"),
    path("<str:user_name>/accept",views.accept,name="accept"),
    path("<str:user_name>/reject",views.reject,name="reject"),
    #path("chats/",views.chat,name="chats")

    
 
]