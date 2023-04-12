from django import forms
from .models import Photocard

class PhotocardForm(forms.ModelForm):
	class Meta:
		model = Photocard
		fields = ('name', 'price', 'is_limited_edition', 'artist', 'member', 'album')