from django import forms

from myrepository.models import Album, Genre, Lending
from django.utils import timezone


BIRTH_YEAR_CHOICES =  range(timezone.now().year - 100, timezone.now().year)

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['title','a_date','favorite','n_songs','description','genres','types'] 

	title = forms.CharField(max_length=100)
	a_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	teste = forms.BooleanField(initial=False, required=False)

class GenreForm(forms.ModelForm):
	class Meta:
		model = Genre
		fields = ('__all__')

class LendingForm(forms.ModelForm):
	class Meta:
		model = Lending
		fields = ('__all__')
