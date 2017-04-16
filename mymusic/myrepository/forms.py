from django import forms

from myrepository.models import Album
from django.utils import timezone


BIRTH_YEAR_CHOICES =  range(timezone.now().year - 100, timezone.now().year)

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['title','a_date','favorite','n_songs','description']

	title = forms.CharField(max_length=100)
	a_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

