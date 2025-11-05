from django.shortcuts import render
import requests
from django.conf import settings

def home(request):
    query = request.GET.get('query', '')
    movies = []

    if query:
        api_key = settings.TMDB_API_KEY
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}"
        response = requests.get(url).json()
        movies = response.get('results', [])

    return render(request, 'movies/home.html', {
        'query': query,
        'movies': movies,
    })
