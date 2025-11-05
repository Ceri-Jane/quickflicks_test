from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests

from .models import Movie


def home(request):
    query = request.GET.get('query', '')
    movies = []

    if query:
        api_key = settings.TMDB_API_KEY
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}"
        response = requests.get(url).json()
        movies = response.get('results', [])

    # ✅ NEW LINE: Get IDs of movies already on the user's shelf
    user_movie_ids = []
    if request.user.is_authenticated:
        user_movie_ids = list(
            Movie.objects.filter(user=request.user).values_list("tmdb_id", flat=True)
        )

    return render(request, 'movies/home.html', {
        'query': query,
        'movies': movies,
        'user_movie_ids': user_movie_ids,   # ✅ This sends it to the template
    })


@login_required
def add_to_shelf(request):
    if request.method == "POST":
        tmdb_id = request.POST.get("movie_id")
        title = request.POST.get("title")
        poster_path = request.POST.get("poster_path")

        movie, created = Movie.objects.get_or_create(
            user=request.user,
            tmdb_id=tmdb_id,
            defaults={
                "title": title,
                "poster_url": f"https://image.tmdb.org/t/p/w200{poster_path}" if poster_path else "",
                "status": "NEW",
            }
        )

    return redirect(request.META.get("HTTP_REFERER", "home"))



@login_required
def my_shelf(request):
    to_put_away = Movie.objects.filter(user=request.user, status="NEW").order_by('title')
    to_watch = Movie.objects.filter(user=request.user, status="TO_WATCH").order_by('title')
    watched = Movie.objects.filter(user=request.user, status="WATCHED").order_by('title')

    return render(request, "movies/shelf.html", {
        "to_put_away": to_put_away,
        "to_watch": to_watch,
        "watched": watched,
    })


@login_required
def remove_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id, user=request.user)
    movie.delete()
    return redirect("my_shelf")



@login_required
def change_status(request, movie_id, new_status):
    movie = Movie.objects.get(id=movie_id, user=request.user)
    movie.status = new_status
    movie.save()
    return redirect("my_shelf")
