from django.contrib import admin
from django.urls import path
from . import views  # Assuming your views are in the same directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game, name='game'),  # Game page
    path('api/lyrics/<int:song_id>/', views.get_lyrics, name='get_lyrics'),  # API to fetch lyrics
    path('api/submit-guess/', views.submit_guess, name='submit_guess'),  # API to submit guesses
]