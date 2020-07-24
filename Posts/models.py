from django.db import models

from accounts.models import User
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.userid.id, filename)

class Posts(models.Model):
    caption = models.TextField(max_length = 2000,null=True)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    Createdon = models.DateField(auto_now=True)
    Updatedon = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=user_directory_path,null=True) 