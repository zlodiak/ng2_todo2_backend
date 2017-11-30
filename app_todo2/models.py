from django.db import models
from django.utils import timezone

class User(models.Model):
  login = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  created_date = models.DateTimeField(
          default=timezone.now)
  published_date = models.DateTimeField(
          blank=True, null=True)

  def __str__(self):
      return self.login