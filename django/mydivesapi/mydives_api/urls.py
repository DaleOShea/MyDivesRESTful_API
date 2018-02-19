from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^diving_locations', views.ListLocations.as_view()),
]
