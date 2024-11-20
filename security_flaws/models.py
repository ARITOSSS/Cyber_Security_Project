from django.db import models

# Create your models here.

class User(models.Model) :
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class UserIDOR(models.Model) : 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name