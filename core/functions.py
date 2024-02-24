from datetime import datetime, timedelta
import os

from django.db.models import Q
from django.http import FileResponse

from core.models import Event


def get_event(slug):
    return Event.objects.get(slug=slug)


def get_upcoming_events():
    current_date = datetime.now()
    three_months_later = current_date + timedelta(days=90)

    upcoming_events = Event.objects.filter(
        Q(time__gte=current_date) & Q(time__lte=three_months_later)
    ).order_by('time')
    return upcoming_events


def get_future_and_past_events():
    current_date = datetime.now()
    past_events = Event.objects.filter(time__lt=current_date).order_by('-time')
    future_events = Event.objects.filter(time__gte=current_date).order_by('time')
    return past_events, future_events


def get_files_from_folder(folder_path):
    return os.listdir(folder_path)


def is_it_file(folder_path, file):
    return os.path.isfile(os.path.join(folder_path, file))


def get_documents_list():
    folder_path = './static/documents'
    files_in_folder = get_files_from_folder(folder_path)
    files = [f for f in files_in_folder if is_it_file(folder_path, f)]
    files = [file.split('.')[0] for file in files]
    return files


def providing_files_for_download_func(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    document_path = f'{base_dir}/static/documents/{file_name}'
    open_document = open(document_path, 'rb')
    response = FileResponse(open_document, as_attachment=True, filename=file_name)
    return response


def sent_email(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    message = form.cleaned_data['message']

    print(name, email, message)
