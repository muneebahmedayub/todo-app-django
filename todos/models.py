from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=255)
    isDone = models.BooleanField(default=False)
