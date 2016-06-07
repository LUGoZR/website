from django import forms
from django.forms import EmailInput, TextInput
from .models import *


class Subscribe(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ('name', 'email')
		widgets = {
			'name': TextInput(attrs={'class': 'btn-xl wow tada', 'placeholder': 'Ime i prezime'}),
			'email': EmailInput(attrs={'class': 'btn-xl wow tada', 'placeholder': 'Email adresa'})
		}


