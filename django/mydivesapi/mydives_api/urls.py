from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register('MyDives', views.MyDivesViewSet, base_name ='MyDives')
router.register('location', views.LocationViewSet, base_name ='location')
router.register('userLogin', views.LoginView, base_name ='User Login')

urlpatterns = [
    url(r'^diving_locations', views.ListLocations.as_view()),
    url(r'^', include(router.urls))
]
