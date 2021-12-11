from django.db import models
from django.db.models.deletion import CASCADE
from account.models import User

# Create your models here.
class ShortStory(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    #perticipents
    context = models.TextField(null = True, blank = True)
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-update','-created']
    
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(ShortStory, on_delete = models.CASCADE)
    body = models.TextField()
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created', '-update']
        
    def __str__(self):
        return self.body[0:100]
    