from django.shortcuts import render, redirect

from core.forms import ContactForm
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

    print(data['events'])
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            functions.sent_email(form)
            return redirect('/')

    return render(request, template, context=data)


def about_us(request):
    template = f'{template_folder}/about-us.html'
    data['title'] = "O NÁS"
    return render(request, template, context=data)


def event(request, slug):
    template = f'{template_folder}/events/event.html'

    this_event = functions.get_event(slug=slug)
    data['title'] = this_event.title
    data['event'] = this_event
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
