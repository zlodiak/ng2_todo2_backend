# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo2', '0004_auto_20171203_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marker',
            name='lng',
            field=models.IntegerField(default=0),
        ),
    ]
