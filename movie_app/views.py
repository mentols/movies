from django.db.models import F, Max, Min, Count, Avg
from django.shortcuts import render, get_object_or_404

from .models import Movie, Director


def show_all_movie(request):
    movies = Movie.objects.order_by(F('rating').asc(nulls_last=True))
    # movies = Movie.objects.order_by('-rating', 'budget')[:2]
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })


def show_director(request, one_director: str):
    dir = Director.objects.get(id=one_director)
    return render(request, 'movie_app/one_director.html', {
        'director': dir
    })
