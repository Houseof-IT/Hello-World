from django.db import models
from accounts.models import User
# Create your models here.

class Friends(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,related_name="friend",on_delete=models.CASCADE)
    pending = models.IntegerField(verbose_name="Request_type", max_length=3, default=0)        
    createdon=models.DateTimeField(auto_now_add=True)
    
