from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

#Importing class USER from django.contrib.auth
#It consists username , password, first name , last name , email id
from django.contrib.auth.models import User
# Create your models here.
#Below is the table for reporter and will be created as
#blog_reporter in Database.

class Reporter(models.Model):
    full_name = models.CharField(max_length=255)

#This will print the name of author/Reporter
    def __str__(self):
        return self.full_name

#Below is the table for articles consists of different columns
#such as publication date , headline , contents , writer name and
#comments by different user. It has foreign relationship with
#Reporter table and hence each column can be accessed by reporter
#table and vice versa.
class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=255)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
#a user login model which will store the images
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    user_commet  = models.OneToOneField(User)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_num = models.IntegerField(default=918015262160)
    email = models.EmailField()
    github = models.CharField(max_length=255)
    #{{object.photo.url}}
    photo = models.ImageField(upload_to="images")
    myaddress = models.TextField(null=True,default="Jharkhand")

    def __str__(self):
        return self.name
