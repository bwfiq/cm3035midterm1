from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie
from .forms import UpdateMovieForm
from django.core.management import call_command
from django.core.management.base import CommandError
import io
import csv

class MovieFormTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            id=1,
            title='Test Movie',
            language='English',
            views=100,
            downloads=50,
            industry='Hollywood',
            runtime=120,
            IMDb_rating=8.0,
            director='Test Director',
            release_date='2022-01-01',
            posted_date='2022-01-02'
        )

    def test_update_movie_form(self):
        form_data = {
            'id': 1,
            'title': 'Updated Movie',
            'language': 'Spanish',
            'views': 150,
            'downloads': 75,
            'industry': 'Bollywood',
            'runtime': 130,
            'IMDb_rating': 7.5,
            'director': 'Updated Director',
            'release_date': '2023-01-01',
            'posted_date': '2023-01-02'
        }
        form = UpdateMovieForm(data=form_data, instance=self.movie)
        self.assertTrue(form.is_valid())

    def test_clean_id_method(self):
        form_data = {
            'id': 2,
            'title': 'Updated Movie',
            'language': 'Spanish',
            'views': 150,
            'downloads': 75,
            'industry': 'Bollywood',
            'runtime': 130,
            'IMDb_rating': 7.5,
            'director': 'Updated Director',
            'release_date': '2023-01-01',
            'posted_date': '2023-01-02'
        }
        form = UpdateMovieForm(data=form_data, instance=self.movie)
        self.assertFalse(form.is_valid())
        self.assertIn('id', form.errors)
