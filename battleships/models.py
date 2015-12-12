from django.conf.app_template import models
from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    salt = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.login


class Game(models.Model):
    firstPlayer = models.OneToOneField(User, related_name="player_one")
    secondPlayer = models.OneToOneField(User, related_name="player_two")

    def __str__(self):
        return str(self.firstPlayer) + " " +  str(self.secondPlayer)
