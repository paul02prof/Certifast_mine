from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("certif/", certification_list, name="certification_list"),
    path('certif_detail/<int:pk>/', certification_detail, name='certification_detail'),
    path("course/",course_list, name="course_list"),
    path('course_detail/<int:pk>/', course_detail, name='course_detail'),

    path('dash/', include('django_plotly_dash.urls')),
path('dashboard/', dashboard, name='dashboard'),
    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
    #path("certification/<int:pk>/", CertificationDetailView.as_view(), name="certification_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
