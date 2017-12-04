# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo2', '0003_auto_20171202_1725'),
    ]

    operations = [
        migrations.AlterField('Marker', 'desc', models.TextField(max_length=255, blank=True, null=True))
    ]
