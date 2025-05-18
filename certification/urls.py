from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import IndexView, AddCertificationView, AddRelatedView, CertificationDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
    path("certification/<int:pk>/", CertificationDetailView.as_view(), name="certification_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
