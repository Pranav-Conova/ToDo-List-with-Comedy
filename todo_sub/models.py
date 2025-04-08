
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    comedy_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

