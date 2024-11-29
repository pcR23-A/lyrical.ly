from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    lyrics = models.TextField()  # Store full lyrics
    difficulty = models.CharField(
        max_length=10, 
        choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')]
    )

    def __str__(self):
        return f"{self.title} by {self.artist}"
