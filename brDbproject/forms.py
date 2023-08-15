from django import forms
from .models import Movies, CastCrew

class Insert_movies(forms.ModelForm):
  class Meta:
    model = Movies
    fields = '__all__'
    labels = {"title": "Title", "summary": "Summary", "year": "Year", "duration": "Duration", "imdb_r": "IMDb rating", "country": "Country", "language": "Language", "movieURL": "Trailer URL", "coverURL": "Cover image URL", }
    help_texts = {
        'duration': "Please insert the duration in minutes",
        'imdb_r': "Please insert a number between 0 and 10",
    }
  castcrews = forms.ModelMultipleChoiceField(
        queryset=CastCrew.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Cast and Crew'
    )

class Insert_castcrew(forms.ModelForm):
    class Meta:
        model = CastCrew
        fields = '__all__'
        labels = {"role": "Role", "name": "Name", "biography": "Biography", "castcrewURL": "Picture URL"}

