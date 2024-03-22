from pathlib import Path
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.db.models import Q
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404

from core.models import Event, FileModel


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


def get_documents_list():
    return FileModel.objects.all()


def providing_files_for_download_func(file_id):
    file_object = get_object_or_404(FileModel, id=file_id)
    file_path = file_object.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_object.file.name}"'
    return response


def providing_db_for_download_func():
    db_file = Path('db.sqlite3')
    if db_file.exists() and db_file.is_file():
        with open(db_file, 'rb') as f:
            response = HttpResponse(f, content_type='application/x-sqlite3')
            response['Content-Disposition'] = 'attachment; filename=db.sqlite3'
            return response
    else:
        return HttpResponse("SQLite database not found", status=404)


def prepare_message(name, email, message):
    message = f"""
        {name}\n 
        {email}\n 
        {message}
    """
    return message

    
def sent_email(form):
    name = f'{form.cleaned_data["name"]} {form.cleaned_data["surname"]}'
    email = form.cleaned_data['email']
    message = form.cleaned_data['message']
    message = prepare_message(name, email, message)

    subject = 'Správa'
    recipient_list = ['vladibuyanov@gmail.com']

    send_mail(
        subject,
        message,
        email,
        recipient_list
    )
