from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import Home
urlpatterns = [
                  path('', Home),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
