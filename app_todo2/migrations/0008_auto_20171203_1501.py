# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo2', '0007_auto_20171203_1454'),
    ]

    operations = [
    	migrations.AlterField('Marker', 'lat', models.CharField(default='0', max_length=20)),
    	migrations.AlterField('Marker', 'lng', models.CharField(default='0', max_length=20))        
    ]
