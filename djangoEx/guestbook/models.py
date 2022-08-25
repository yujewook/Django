from django.db import models
from _datetime import datetime

# Create your models here.
class Guestbook (models.Model):
    idx = models.AutoField (primary_key = True)
    name = models.CharField(null=False, max_length=50)
    email = models.CharField(null=True, max_length=50)
    passwd = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    postdate = models.DateTimeField(default = datetime.now, blank=True)