from django.db import models

class Singer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Meta:
    app_label = 'song'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'