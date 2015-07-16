# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=7, verbose_name='\u0412\u0438\u043a\u043e\u043d\u0430\u0432\u0435\u0446\u044c')),
                ('composition_name', models.CharField(max_length=7, verbose_name='\u041f\u0456\u0441\u043d\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0456\u0441\u043d\u044f',
                'verbose_name_plural': '\u041f\u0456\u0441\u043d\u0456',
            },
            bases=(models.Model,),
        ),
    ]
