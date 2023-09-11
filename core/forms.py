from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Meno', max_length=100)
    surname = forms.CharField(label='Priezvisko', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Správa', widget=forms.Textarea(attrs={'rows': 6}))
