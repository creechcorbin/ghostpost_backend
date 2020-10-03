from django.db import models
from datetime import datetime

# Create your models here.

class Boast(models.Model):
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    post_time = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-post_time']

    def votescore(self):
        return self.up_votes - self.down_votes

class Roast(models.Model):
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField()
    post_time = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-post_time']

    def votescore(self):
        return self.up_votes - self.down_votes