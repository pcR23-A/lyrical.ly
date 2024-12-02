from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Lyrics(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, related_name='lyrics')
    text = models.TextField()

    def __str__(self):
        return f"Lyrics for {self.song.title}"

class LyricWord(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=50)
    position = models.IntegerField()

    def __str__(self):
        return f"{self.word} at position {self.position} in {self.song.title}"