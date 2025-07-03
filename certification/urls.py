from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("certif/", certification_list, name="certification_list"),
    path('certif_detail/<int:pk>/', certification_detail, name='certification_detail'),
    path("course/",course_list, name="course_list"),
    path('course_detail/<int:pk>/', course_detail, name='course_detail'),
    path("path/",path_user, name="path"),

    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('dash/', include('django_plotly_dash.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
