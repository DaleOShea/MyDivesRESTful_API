from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register('MyDives', views.MyDivesViewSet)

urlpatterns = [
    url(r'^diving_locations', views.ListLocations.as_view()),
    url(r'^', include(router.urls))
]
