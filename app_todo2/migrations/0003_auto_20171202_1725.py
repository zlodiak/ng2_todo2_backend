# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo2', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('desc', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='user_id',
            field=models.ForeignKey(null=True, to='app_todo2.User', blank=True, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='marker',
            name='todo',
            field=models.ForeignKey(null=True, to='app_todo2.Todo', blank=True, verbose_name='Todo'),
        ),
    ]
