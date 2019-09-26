

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('upload/', upload, name='upload'),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),

]
