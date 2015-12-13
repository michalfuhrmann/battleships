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
        return self.username


class Game(models.Model):
    OPEN = 'o'
    IN_PROGRESS = 'w'
    END = 'z'
    STATES = (
        (OPEN, 'otwarta'),
        (IN_PROGRESS, 'w trakcie'),
        (END, 'zakonczona'),
    )

    firstPlayer = models.OneToOneField(User, related_name="player_one")
    secondPlayer = models.OneToOneField(User, related_name="player_two", null=True)
    status = models.CharField(max_length=1, choices=STATES, default=OPEN)
    date = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        for state in Game.STATES:
            if state[0] == self.status:
                return state[1]

    def __str__(self):
        return str(self.firstPlayer) + " " + str(self.secondPlayer) + str(self.status)
