from django.db import models

from user_app.models import User

# Create your models here.


class Todo(models.Model):

    user =models.ForeignKey(User,on_delete=models.CASCADE)

    priority_choices= [('high','high'),
                        ('low','low')]
    
    priority = models.CharField(max_length=50,choices=priority_choices)

    task_name = models.CharField(max_length=100)

    created_date = models.DateField(auto_now_add=True)

    is_completed = models.BooleanField(default=False)
