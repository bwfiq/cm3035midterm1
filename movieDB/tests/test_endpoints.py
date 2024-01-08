from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from movieDB.models import Movie

class EndpointTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            id=1,
            title="Test Movie",
            language="English",
            views=100,
            downloads=50,
            industry="Hollywood",
            runtime=120,
            IMDb_rating=7.5,
            director="Test Director",
            release_date="2022-01-01",
            posted_date="2022-01-01",
        )

    def test_get_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")

    def test_get_movie_detail(self):
        url = reverse('movie-detail', args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")

    def test_post_movie_create(self):
        url = reverse('movie-list')
        data = {
            'title': 'New Movie',
            'language': 'Spanish',
            'views': 200,
            'downloads': 100,
            'industry': 'Hollywood',
            'runtime': 110,
            'IMDb_rating': 8.0,
            'director': 'New Director',
            'release_date': '2022-02-01',
            'posted_date': '2022-02-01',
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Movie.objects.filter(title='New Movie').exists())

