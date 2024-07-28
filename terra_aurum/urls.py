from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from core import views


urlpatterns = [
    path('', RedirectView.as_view(url='/app/')),
    path('app/', include('core.urls')),

    path('admin/download-db/', views.download_db, name='download_db'),
    path('admin/', admin.site.urls),
]
