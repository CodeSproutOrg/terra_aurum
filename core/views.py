from datetime import datetime, timedelta

from django.shortcuts import render

from django.db.models import Q
from core.models import Event


template_folder = 'pages'
menu = {
    'O NÁS': '/about-us',
    'PODUJATIA': '/events',
    'KONTAKTY': '/contacts',
    'DOKUMENTY': '/documents'
}


def index(request):
    template = f'{template_folder}/index.html'
    data = {"title": "TERRA-AURUM", "menu": menu}

    current_date = datetime.now()
    three_months_later = current_date + timedelta(days=90)

    upcoming_events = Event.objects.filter(Q(time__gte=current_date) & Q(time__lte=three_months_later)).order_by('time')
    data['events'] = upcoming_events

    return render(request, template, context=data)


def about_us(request):
    template = f'{template_folder}/about-us.html'
    data = {"title": "O NÁS", "menu": menu}
    return render(request, template, context=data)


def event(request, slug):
    template = f'{template_folder}/events/event.html'

    this_event = Event.objects.get(slug=slug)
    data = {
        "title": this_event.title,
        "menu": menu,
        'event': this_event
    }
    return render(request, template, context=data)


def events(request):
    template = f'{template_folder}/events/events.html'
    data = {"title": "PODUJATIA", "menu": menu}

    current_date = datetime.now()
    past_events = Event.objects.filter(time__lt=current_date).order_by('-time')
    future_events = Event.objects.filter(time__gte=current_date).order_by('time')

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
    data = {"title": "Neexistuje", "menu": menu}
    template = 'errors/404.html'
    return render(request, template, context=data, status=404)
