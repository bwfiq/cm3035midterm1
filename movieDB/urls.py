from django.urls import path
from .views import MovieListView, MovieListCreateView, MovieDetailView, LongestMoviesView, ShortestMoviesView, TopDownloadsView, add_movie, MovieUpdateView
urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('top-downloads/', TopDownloadsView.as_view(), name='top-downloads'),
    path('movies/longest/', LongestMoviesView.as_view(), name='longest-movies'),
    path('movies/shortest/', ShortestMoviesView.as_view(), name='shortest-movies'),
    path('add-movie/', add_movie, name='add-movie'),
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='update-movie'),
]