from django.urls import path
from apps.ADMIN.views import  ClientListAPIView,ClientCUDAPIView


from rest_framework.routers import DefaultRouter, SimpleRouter



app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register('client/list',ClientListAPIView,basename="client-list")
router.register('client/cud',ClientCUDAPIView,basename="client-cud")

urlpatterns = [
] + router.urls
