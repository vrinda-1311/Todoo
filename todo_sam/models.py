from django.db import models

# Create your models here.

class TodoModel(models.Model):

    name = models.CharField(max_length=50)

    task_name = models.CharField(max_length=100)

    is_completed = models.BooleanField(default=False)
