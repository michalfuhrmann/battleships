# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstPlayer', models.OneToOneField(related_name='player_one', to='battleships.User')),
                ('secondPlayer', models.OneToOneField(related_name='player_two', to='battleships.User')),
            ],
        ),
    ]
