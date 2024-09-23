from django import forms
from .models import Reservation


class ContactForm(forms.Form):
    name = forms.CharField(label='Meno', max_length=100)
    surname = forms.CharField(label='Priezvisko', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Správa', widget=forms.Textarea(attrs={'rows': 6}))


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'tickets']
        labels = {
            'name': 'Meno',
            'email': 'E-mail',
            'tickets': 'Počet lístkov',
        }
