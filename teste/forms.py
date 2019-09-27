from django import forms 
from .models import Teste


class TesteForm(forms.ModelForm):

	class Meta:
		model = Teste
		fields = ('title', 'description')