from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()

urlpatterns = [
] + router.urls
