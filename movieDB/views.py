from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .forms import MovieForm, UpdateMovieForm, ReadOnlyMovieForm
from .serializers import MovieSerializer

class MovieListView(ListView):
    model = Movie
    template_name = 'movieDB/movie_list.html'
    context_object_name = 'movies'

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TopDownloadsView(APIView):
    def get(self, request, format=None):
        top_movies = Movie.objects.order_by('-downloads')[:10]
        serializer = MovieSerializer(top_movies, many=True)
        return Response(serializer.data)
    
class LongestMoviesView(generics.ListAPIView):
    queryset = Movie.objects.order_by('-runtime')[:5]
    serializer_class = MovieSerializer

class ShortestMoviesView(generics.ListAPIView):
    queryset = Movie.objects.order_by('runtime')[:5]
    serializer_class = MovieSerializer

class MovieUpdateView(View):
    template_name = 'movieDB/update_movie.html'

    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        form = ReadOnlyMovieForm(instance=movie)
        return render(request, self.template_name, {'form': form, 'movie': movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        form = UpdateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        else:
            errors = form.errors
            return render(request, self.template_name, {'form': form, 'movie': movie, 'errors': errors})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list-create')
    else:
        form = MovieForm()

    return render(request, 'movieDB/add_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, id=pk)

    if request.method == 'POST':
        form = UpdateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list-create')
    else:
        form = UpdateMovieForm(instance=movie)

    return render(request, 'movieDB/update_movie.html', {'form': form, 'movie': movie})