from django.contrib import admin
from django.urls import path
from analisis_sentimen.views import *
from django.views.static import serve
from django.conf.urls.static import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload, name='upload'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]