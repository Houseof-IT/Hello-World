from django.shortcuts import render,HttpResponse
from friends.models import Friends
from accounts.models import User
# Create your views here.
def Chats(request):
    usr=request.user
    frnd=Friends.objects.filter(user1=usr).all()
    usr=[]
    for i in range(0,len(frnd)):
        usr.append(User.objects.get(id=frnd[i].id))
        print(frnd[i],usr[i].id)
    return render(request,"chats/chats_list.html",{'frnds':usr})
