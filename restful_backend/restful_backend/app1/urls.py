from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', list_view),
    path('detail/<pk>',login_detail_view)
]
