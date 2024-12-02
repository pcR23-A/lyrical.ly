from lirically.models import Song, LyricWord

# Assuming the song already exists
song = Song.objects.get(title="Twinkle Twinkle Little Star")

lyrics_text = """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!
"""

# Split lyrics into words and store each word with its position
words = lyrics_text.replace('\\n', ' ').split()
for position, word in enumerate(words):
    LyricWord.objects.create(song=song, word=word.strip(',.!?'), position=position)