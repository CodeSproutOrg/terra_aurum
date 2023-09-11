from datetime import datetime, timedelta


from django.db.models import Q

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


def sent_email(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    message = form.cleaned_data['message']

    print(name, email, message)
