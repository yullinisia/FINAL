from django.db import models

class Singer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Born', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        app_label = 'song'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'