from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean_id(self):
        movie_id = self.cleaned_data['id']

        # Check if the movie ID is an integer
        try:
            movie_id = int(movie_id)
        except ValueError:
            raise forms.ValidationError("Movie ID must be an integer.")

        # Check if the movie ID already exists
        if Movie.objects.filter(id=movie_id).exists():
            raise forms.ValidationError("Movie with this ID already exists.")

        return movie_id
    
class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean_id(self):
        # Ensure that the 'id' field remains unchanged
        cleaned_id = self.cleaned_data['id']
        instance_id = self.instance.id if self.instance else None

        if instance_id is not None and cleaned_id != instance_id:
            raise forms.ValidationError("The 'id' field cannot be changed.")

        return cleaned_id

class ReadOnlyMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            field: forms.TextInput(attrs={'readonly': True}) for field in fields
        }