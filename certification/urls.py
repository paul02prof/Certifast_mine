from django.urls import path
from .views import IndexView, AddCertificationView, AddRelatedView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
]
