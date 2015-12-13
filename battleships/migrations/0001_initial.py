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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[('o', 'otwarta'), ('w', 'w trakcie'), ('z', 'zakonczona')], default='o')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('salt', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='firstPlayer',
            field=models.OneToOneField(to='battleships.User', related_name='player_one'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondPlayer',
            field=models.OneToOneField(null=True, to='battleships.User', related_name='player_two'),
        ),
    ]
