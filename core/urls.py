from django.urls import path

from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us'),
    path('contacts', views.contacts, name='contacts'),

    path('events', views.events, name='events'),
    path('events/<slug:slug>/', views.event, name='event'),

    path('documents', views.documents, name='documents'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
