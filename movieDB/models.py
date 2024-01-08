from django.db import models

class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    views = models.PositiveIntegerField()
    downloads = models.PositiveIntegerField()
    industry = models.CharField(max_length=100)
    runtime = models.PositiveIntegerField()
    IMDb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    posted_date = models.DateField()

    class Meta:
        app_label = 'movieDB'

    def __str__(self):
        return self.title