from django.db import models
from datetime import date


class Task(models.Model):
    title = models.CharField("Task name", max_length=50)
    description = models.TextField('Description')
    date = models.DateField(default=date.today())
    date_end = models.DateField(null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"
