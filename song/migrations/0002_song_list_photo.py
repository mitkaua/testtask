# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_list',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
    ]
