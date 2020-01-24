from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('success', display_images, name='display_images'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
