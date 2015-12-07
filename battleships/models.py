from django.conf.app_template import models
from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.login


class Game(models.Model):
    firstPlayer = models.OneToOneField(User, related_name="player_one")
    secondPlayer = models.OneToOneField(User, related_name="player_two")

    def __str__(self):
        return str(self.firstPlayer) + " " +  str(self.secondPlayer)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text;

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
