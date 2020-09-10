from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL 
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    class Meta:
        ordering = ["-id"]

    def serialize(self):
        return {
            "id": self.id,
            "content":self.content,
            "Likes": random.randint(0, 200)
        }