from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us'),
    path('events', views.events, name='events'),
    path('documents', views.documents, name='documents'),

    path('admin/', admin.site.urls),
]
