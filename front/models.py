from django.db import models
from django.contrib.auth.models import User # i have to import user so that it can be accessible

# Create your models here.

# this is for the topic name 
class Topic(models.Model):
   name  = models.CharField(max_length=200)

   # I want to have the name of topic in order form
   class Meta():
      ordering = ('name',)

   # I have to return the name of the topic
   def __str__(self):
      return self.name

# this is for the room i have created
class Room(models.Model):
   host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
   name = models.CharField(max_length=200)
   description = models.TextField(null=True, blank=True)
   # participants = 
   updates = models.DateTimeField(auto_now=True)
   created = models.DateTimeField(auto_now_add=True)

   # I want to have the name of topic in order form
   class Meta():
      ordering = ['-updates', '-created']


   # I have to return the name of the topic
   def __str__(self):
      return self.name

# i will need to have meassages for the users
class Message(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   body = models.TextField()
   updates = models.DateTimeField(auto_now=True)
   created = models.DateTimeField(auto_now_add=True)


   # I want to have the name of topic in order form
   class Meta():
      ordering = ('-created', '-updates')


   # I have to return the name of the topic
   def __str__(self):
      return self.body[0:60]
