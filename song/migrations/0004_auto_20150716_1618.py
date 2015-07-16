# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_auto_20150716_1606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song_list',
            new_name='Song',
        ),
    ]
