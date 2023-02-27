from django.db import models

0
class TodoList(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)

    # def to_json(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name
    #     }


class Todo(models.Model):
    name = models.CharField(max_length=255, null=False)
    done = models.BooleanField(default=False, null=False)
    todo_list = models.ForeignKey(TodoList, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)