from django.db import models
from django.utils import timezone

class User(models.Model):
  login = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.login


class Todo(models.Model):
  user_id = models.ForeignKey(User, verbose_name=u"Пользователь", blank=True, null=True,)
  title = models.CharField(max_length=100)
  isCompleted = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.title + ' ' + str(self.isCompleted)


class Marker(models.Model):
  todo = models.ForeignKey(Todo, verbose_name=u"Todo", blank=True, null=True,)
  desc = models.CharField(max_length=300)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return str(self.created_date)
