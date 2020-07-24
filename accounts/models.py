from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profilepic/{1}'.format(instance.id, filename)

class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,error_messages={'unique': "A user with that email already exists.",}) 
    Countrycode = models.CharField(max_length=10)
    Phone_no = models.DecimalField(max_digits=10,decimal_places=0)
    Birthday = models.DateTimeField()
    Gender = models.CharField(max_length=6)
    Isactivated=models.BooleanField(default=True)
    Issuspended=models.BooleanField(default=False)
    Bio=models.TextField()
    Count=models.IntegerField(default=0)
    
    profilepic = models.ImageField(upload_to=user_directory_path, blank=True,default="profile_pic/default.png")
