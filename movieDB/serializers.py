from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
    def validate(self, data):
        imdb_rating = data.get('IMDb_rating')
        if imdb_rating is not None and (imdb_rating < 0 or imdb_rating > 10):
            raise serializers.ValidationError("IMDb rating must be between 0 and 10.")

        # You can add more validation checks as needed

        return data