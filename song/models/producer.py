from django.db import models

class Producer(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        app_label = 'song'

    def __str__(self):
        return f'{self.name}'
