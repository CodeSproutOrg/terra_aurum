from django.shortcuts import render, redirect

from core.forms import ContactForm
from core.functions import get_upcoming_events, sent_email, get_event, get_future_and_past_events


template_folder = 'pages'
menu = {
    'O NÁS': '/about-us',
    'PODUJATIA': '/events',
    'KONTAKTY': '/contacts',
    'DOKUMENTY': '/documents'
}


def index(request):
    template = f'{template_folder}/index.html'
    data = {
        "title": "TERRA-AURUM",
        "menu": menu,
        'events': get_upcoming_events()
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sent_email(form)
            return redirect('/')
    else:
        form = ContactForm()
    data['form'] = form
    return render(request, template, context=data)


def about_us(request):
    template = f'{template_folder}/about-us.html'
    data = {"title": "O NÁS", "menu": menu}
    return render(request, template, context=data)


def event(request, slug):
    template = f'{template_folder}/events/event.html'

    this_event = get_event(slug=slug)
    data = {
        "title": this_event.title,
        "menu": menu,
        'event': this_event
    }
    return render(request, template, context=data)


def events(request):
    template = f'{template_folder}/events/events.html'
    data = {"title": "PODUJATIA", "menu": menu}

    past_events, future_events = get_future_and_past_events()
    data['past_events'] = past_events
    data['future_events'] = future_events

    return render(request, template, context=data)


def contacts(request):
    template = f'{template_folder}/contacts.html'
    data = {"title": "KONTAKTY", "menu": menu}

    return render(request, template, context=data)


def documents(request):
    template = f'{template_folder}/documents.html'
    data = {"title": "DOKUMENTY", "menu": menu}
    return render(request, template, context=data)


def view_404(request, exception):
    template = 'errors/404.html'
    data = {"title": "Neexistuje", "menu": menu}
    return render(request, template, context=data, status=404)
