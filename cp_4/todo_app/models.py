from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=50)

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
