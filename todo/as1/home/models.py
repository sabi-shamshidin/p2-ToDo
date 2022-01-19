from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=250)
    during = models.DateField()

    def __str__(self):
        return self.title
