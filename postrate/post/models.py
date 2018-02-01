from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.post_text



