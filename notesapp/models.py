from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 👈 added
    updated_at = models.DateTimeField(auto_now=True)      # 👈 optional but nice
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

        