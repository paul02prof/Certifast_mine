from django.urls import path
from .views import index, add_certification

urlpatterns = [
    path("", index, name="index"),
    path("add/", add_certification, name="add_certification"),
]
