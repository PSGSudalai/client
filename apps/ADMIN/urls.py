from django.urls import path
from apps.ADMIN.views import (
    ClientListAPIView,
    ClientCUDAPIView,
    InvoiceListAPIView,
    InvoiceCUDAPIView,
    ProjectListAPIView,
    ProjectCUDAPIView,
    MeetingListAPIView,
    MeetingCUDAPIView,

) 


from rest_framework.routers import DefaultRouter, SimpleRouter




app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register('client/list',ClientListAPIView,basename="client-list")
router.register('client/cud',ClientCUDAPIView,basename="client-cud")

router.register('invoice/list',InvoiceListAPIView,basename="invoice-list")
router.register('invoice/cud',InvoiceCUDAPIView,basename="invoice-cud")


router.register('project/list',ProjectListAPIView,basename="project-list")
router.register('project/cud',ProjectCUDAPIView,basename="project-cud")

router.register('meeting/list',MeetingListAPIView,basename="meeting-list")
router.register('meeting/cud',MeetingCUDAPIView,basename="meeting-cud")

urlpatterns = [
] + router.urls
