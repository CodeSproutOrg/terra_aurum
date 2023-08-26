from django.contrib import admin
from django.urls import path

from core import views

handler404 = 'core.views.view_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us'),
    path('events', views.events, name='events'),
    path('events/<slug:slug>/', views.event, name='event'),
    path('contacts', views.contacts, name='contacts'),
    path('documents', views.documents, name='documents'),

    path(r'404', views.view_404),

    path('admin/', admin.site.urls),
]
