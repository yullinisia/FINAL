from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey('Singer', on_delete=models.SET_NULL, null=True)
    album = models.ManyToManyField(Album)
    date_published = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Singer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'