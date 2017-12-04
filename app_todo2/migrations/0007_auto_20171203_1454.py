# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo2', '0006_auto_20171203_1437'),
    ]

    operations = [
    	migrations.AlterField('Marker', 'lat', models.DecimalField(default=0, max_digits=20, decimal_places=16)),
    	migrations.AlterField('Marker', 'lng', models.DecimalField(default=0, max_digits=20, decimal_places=16))    
    ]
