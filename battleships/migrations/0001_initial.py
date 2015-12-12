# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.CharField(max_length=1, choices=[('o', 'otwarta'), ('w', 'w trakcie'), ('z', 'zakonczona')])),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(unique=True, max_length=25)),
                ('salt', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='firstPlayer',
            field=models.OneToOneField(related_name='player_one', to='battleships.User'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondPlayer',
            field=models.OneToOneField(related_name='player_two', to='battleships.User'),
        ),
    ]
