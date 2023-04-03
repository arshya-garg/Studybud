from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
          return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        room = models.ForeignKey(Room, on_delete=models.CASCADE)
        body = models.TextField()
        updated = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
               ordering = ['-updated', '-created']

        def __str__(self):
             return self.body[0:50]




# TOPICS CAN HAVE MULTIPLE ROOMS BUT A ROOM CAN HAVE ONLY ONE Topic

# DJango user model

# when parent is deleted, child is set null or cascaded

    
    # To add model to database: first we need to make migrations by ( basically list of sql commands and add it to the database)
    # thus, python manage.py makemigrations
    # 0001_inital is inital migration
    # After making migrations, we need to apply by python manage.py migrate

    # now open admin page and login
    # for setting up admin: 
    # use python manage.py createsuperuser and type details


    # models by default have an id generated for them