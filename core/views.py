from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from core.models import Event
from core.forms import ContactForm, ReservationForm
from core import functions

app = '/app'
template_folder = 'core/pages'
data = {
    'menu': {
        'O NÁS': f'{app}/about-us',
        'PODUJATIA': f'{app}/events',
        'KONTAKTY': f'{app}/contacts',
        'DOKUMENTY': f'{app}/documents'
    }
}


def index(request):
    template = f'{template_folder}/index.html'
    data['title'] = "TERRA-AURUM"
    data['events'] = functions.get_upcoming_events()
    data['form'] = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            functions.sent_email(form)
            return redirect('/')

    return render(request, template, context=data)


def event(request, slug):
    template = f'{template_folder}/events/event.html'
    this_event = get_object_or_404(Event, slug=slug)
    data = {
        'title': this_event.title,
        'event': this_event,
        'available_tickets': this_event.available_tickets
    }

    if this_event.requires_reservation:
        form = ReservationForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            reservation = form.save(commit=False)
            reservation.event = this_event

            if reservation.tickets <= this_event.available_tickets:
                this_event.available_tickets -= reservation.tickets
                this_event.save()
                reservation.save()
                messages.success(request, 'Vaša rezervácia bola úspešne vykonaná')
                return redirect('event', slug=slug)
            else:
                message = f'Bohužiaľ, nie je dostatok lístkov. K dispozícii je len {this_event.available_tickets} lístkov.'
                messages.error(request, message)

        data['form'] = form

    else:
        data['message'] = "Na toto podujatie nie je potrebné rezervovať si vstupenky."

    return render(request, template, context=data)

def about_us(request):
    template = f'{template_folder}/about-us.html'
    data['title'] = "O NÁS"
    return render(request, template, context=data)


def events(request):
    template = f'{template_folder}/events/events.html'
    past_events, future_events = functions.get_future_and_past_events()

    data['title'] = "PODUJATIA"
    data['past_events'] = past_events
    data['future_events'] = future_events

    return render(request, template, context=data)


def contacts(request):
    template = f'{template_folder}/contacts.html'
    data['title'] = "KONTAKTY"

    return render(request, template, context=data)


def documents(request):
    template = f'{template_folder}/documents.html'
    data['title'] = "DOKUMENTY"
    data['documents'] = functions.get_documents_list()

    return render(request, template, context=data)


def download_file(request, file_id):
    return functions.providing_files_for_download_func(file_id)


def view_404(request, exception):
    template = 'errors/404.html'
    data['title'] = "Neexistuje"
    return render(request, template, context=data, status=404)


def download_db(request):
    return functions.providing_db_for_download_func()
