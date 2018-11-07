from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return 'Artist: ' + self.artist + 'Title Of Album: ' + self.album_title + \
               'Genre: ' + self.genre


class Description(models.Model):
    album = models.CharField(max_length=9999)
    description = models.CharField(max_length=99999)
    song_text = models.CharField(max_length=99999)

    def __str__(self):
        return self.description

