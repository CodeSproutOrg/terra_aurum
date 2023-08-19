from django.shortcuts import render

from core.models import Event

template_folder = 'pages'
menu = {
    'O NÁS': '/about-us',
    'PODUJATIA': '/events',
    'NAŠE AKTIVITY': '',
    'KONTAKT': '',
    'DOKUMENTY': '/documents'
}


def index(request):
    template = f'{template_folder}/index.html'
    data = {"title": "TERRA-AURUM", "menu": menu}
    return render(request, template, context=data)


def about_us(request):
    template = f'{template_folder}/about-us.html'
    data = {"title": "O NÁS", "menu": menu}
    return render(request, template, context=data)


def events(request):
    template = f'{template_folder}/events.html'
    data = {"title": "PODUJATIA", "menu": menu}

    all_events = Event.objects.all()
    data['all_events'] = all_events

    return render(request, template, context=data)


def event(request, slug):
    template = f'{template_folder}/event.html'

    this_event = Event.objects.get(slug=slug)
    data = {
        "title": this_event.title,
        "menu": menu,
        'event': this_event
    }
    return render(request, template, context=data)


def documents(request):
    template = f'{template_folder}/documents.html'
    data = {"title": "DOKUMENTY", "menu": menu}
    return render(request, template, context=data)
