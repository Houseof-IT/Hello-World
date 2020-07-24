from django.shortcuts import render,redirect
from .models import Friends
from accounts.models import User
from Posts.models import Posts
# Create your views here.
def findf(request,user_name):
    usrnm = request.user
    
    if usrnm.username == user_name:
       print("This is the logged in user.")
       return redirect('accounts:profile')
    print(usrnm.id)
    users= User.objects.filter(username=usrnm)
    data = User.objects.filter(username=user_name)
    #frnd = User.objects.filter(username__iexact=user_name).first()
    pos = Posts.objects.filter(userid__id__in=data)
    frnds = Friends.objects.filter(user1__id__in=users,user2__id__in=data).exists()
    print("Exists frnd : ",frnds)

    if frnds == False:
        return render(request,'accounts/friends.html',{'data':data,"pos":pos,"frns":frnds})
       
    elif frnds is True:
        frnd=Friends.objects.get(user1__id__in=users,user2__id__in=data)
        print(frnd.pending)
        if frnd.pending is 0 or frnd.pending is 1 or frnd.pending is 2 :
            return render(request,"accounts/friends.html",{'data':data,"pos":pos,"frnds":frnd.pending})        
       
