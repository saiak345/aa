from django.urls import path
from hug.views import home
urlpatterns = [
    path('',home),
]
