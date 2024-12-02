from django.shortcuts import render
from django.http import JsonResponse
from .models import Song, Lyrics

# View for the game page
def game(request):
    return render(request, 'game.html')

# API view to fetch lyrics for a specific song
def get_lyrics(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
        lyrics = song.lyrics.text
        return JsonResponse({'lyrics': lyrics})
    except Song.DoesNotExist:
        return JsonResponse({'error': 'Song not found'}, status=404)

# API view to submit a guess and return feedback
def submit_guess(request):
    if request.method == 'POST':
        guess = request.POST.get('guess', '')
        # Placeholder for guess checking logic
        # For now, just return the guess as feedback
        return JsonResponse({'feedback': f'Your guess: {guess}'})
    return JsonResponse({'error': 'Invalid request'}, status=400)