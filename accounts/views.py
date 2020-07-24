from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import User
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from Posts.models import Posts
from django.contrib.auth.decorators import login_required
from friends.models import Friends


# Create your views here.
def index(request):
    return render(request,'accounts/Login.html')
def register(request):
    return render(request,'accounts/register.html')

def registers(request):
    if request.method == 'POST':
        First_name=request.POST['fname']
        Last_name = request.POST['lname']
        Email = request.POST['email']
        Phone_no = request.POST['phoneno']
        Countrycode= request.POST['countryCode']
        Birthday = request.POST['bday']
        Gender = request.POST.get('gender')
        print(Gender)
        Username = request.POST['uname']
        Password=request.POST['pass1']

        exists = User.objects.filter(username=Username).exists()
        if(exists is True):
            return HttpResponse("<h1>User already exists</h1>")
        else:    
            user=User.objects.create(first_name=First_name,last_name=Last_name,email=Email,Countrycode=Countrycode,Phone_no=Phone_no,Birthday=Birthday,Gender=Gender,username=Username)
            user.set_password(Password)
            user.save()
            print("User Created")
            return redirect('/')
    else:
            return HttpResponse("<b>Problem</b>")


def logins(request):
    username = request.POST['Username']
    password = request.POST.get('Password','')
    user= authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('accounts:profile')
    else:
        return redirect("/")
@login_required
def profile(request):
    if request.user_agent.is_mobile:
        print("You are using mobile")
    else:
        print("You are using PC")
    usrnm = request.user
    ip_address = request.META.get('REMOTE_ADDR','')
    print("Ip Address : ",ip_address," ", usrnm)
    data = User.objects.filter(username=usrnm)
    posts = Posts.objects.filter(userid__id__in=data)
    return render(request,'accounts/profile.html',{'data':data,'posts':posts})
def home(request):
    usrnm = request.user
    ip_address = request.META.get('REMOTE_ADDR','')
    print("Ip Address : ",ip_address)
    data = User.objects.filter(username=usrnm)
    posts = Posts.objects.filter(userid__id__in=data)
    return render(request,'accounts/home.html',{'datas':data,'posts':posts})

def post(request):
    usr = request.user
    user1=User.objects.get(username=usr)

    status=request.POST.get('text')
    img = request.FILES['image']
    posts = Posts.objects.create(userid=user1,caption=status,image=img)
    posts.save()
    #from PIL import Image
    #img=Image.open(request.FILES['images'])
    #img.save(fp="max.jpg")
    return redirect('accounts:home')
@login_required
def friendsf(request):
    print(request.GET.get("search"))
    searchq=request.GET.get("search")
    searchqs =searchq.split()
    print(len(searchqs))
    if len(searchqs)>1:
        users=User.objects.all().filter(Q(username=searchq)|Q(first_name=searchqs[0])|Q(last_name=searchqs[1])|Q(first_name=searchq)|Q(last_name=searchq))
    else:
        users=User.objects.all().filter(Q(username=searchq)|Q(first_name=searchq)|Q(last_name=searchq))
    print(users)
    return render(request,"accounts/search.html",{'results':users})
def upprof(request):
    usrnm =request.user

    data = User.objects.get(username=usrnm)

    data.profilepic = request.FILES['prof']
    data.save()
    return redirect('accounts:profile')

def updatebio(request):
    usr=request.user
    bio=request.POST['bio']
    data = User.objects.get(username=usr)
    data.Bio=bio
    data.save()
    return redirect('accounts:profile')
def logouts(request):
    logout(request)
    return redirect('/')

def forgot(request):
    return render(request,'accounts/forgot.html')

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
       
def follow(request,user_name):
    usrnm = request.user
    data=User.objects.get(username__iexact=user_name)
    frnd = Friends.objects.create(user1=usrnm,user2=data,pending=0)
    frnd.save()
    return redirect('accounts:home')

def accept(request,user_name):
    usrnm = request.user
    users= User.objects.filter(username=usrnm)
    data = User.objects.filter(username=user_name)
    frnds = Friends.objects.filter(user1__id__in=users,user2__id__in=data).update(pending = 1)
    
    return redirect('accounts:profile')

def reject(request,user_name):
    usrnm = request.user
    users= User.objects.filter(username=usrnm)
    data = User.objects.filter(username=user_name)
    frnds = Friends.objects.filter(user1__id__in=users,user2__id__in=data).update(pending = 2)
    return HttpResponseRedirect ('{0}',user_name)
#def chat(request):
 #   return HttpResponse("Hello World")