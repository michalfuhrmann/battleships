# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='secondPlayer',
            field=models.OneToOneField(null=True, related_name='player_two', to='battleships.User'),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(max_length=1, default='o', choices=[('o', 'otwarta'), ('w', 'w trakcie'), ('z', 'zakonczona')]),
        ),
    ]
