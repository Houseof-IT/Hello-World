from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name="chats"
urlpatterns=[
        path('chat_list',views.Chats,name="chat_list"),
      
]