#from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from PIL import Image


class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    #uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    #date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.caption


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    #starred = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title



