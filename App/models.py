from enum import unique
from pickle import TRUE
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0,'draft'),(1,'published'))
class Post(models.Model):
    # title = models. CharFields(max_length = 200, unique=TRUE)
    title = models.CharField(max_length=200,unique=TRUE)
    #slug = models.SlugFields(max_length = 200, unique=TRUE)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)

    
    class Meta:
        ordering = ["-create_on"]

    def _str_(self):
        return self.title