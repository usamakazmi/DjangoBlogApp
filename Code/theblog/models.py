from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class SentData(models.Model):
    comment = models.TextField()
    commentDate = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    sentiment = models.CharField(max_length = 255)
    ownerData = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    
    
class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, default = "My Awesome Blog")
    
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length = 255, default = 'coding')

    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')