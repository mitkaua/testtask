# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_song_list_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_list',
            name='artist_name',
            field=models.CharField(max_length=250, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u0432\u0435\u0446\u044c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song_list',
            name='composition_name',
            field=models.CharField(max_length=250, verbose_name='\u041f\u0456\u0441\u043d\u044f'),
            preserve_default=True,
        ),
    ]
