from django.db import models
from users.models import User  
# Create your models here.
class Tags(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    created_at = models.DateTimeField(auto_now=True)
    

class notes(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length = 100)
    content = models.TextField(null = True, blank = True)
    tags = models.ManyToManyField(Tags, related_name = 'Tags Model',on_delete= models.CASCADE )
    user = models.ForeignKey(User, related_name = "Users Model", on_delete= models.CASCADE )
    is_pinned = models.BooleanField(default = False)
    is_deleted = models.BooleanField(default = False) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
