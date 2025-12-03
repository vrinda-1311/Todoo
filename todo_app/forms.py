from django import forms

from todo_app.models import Todo

class TaskForm(forms.ModelForm):

    class Meta:

        model = Todo

        fields = ['priority','task_name',]