from django.urls import path
from apps.ADMIN.models import DocumentFile
from apps.ADMIN.views import (
    ClientListAPIView,
    ClientCUDAPIView,
    InvoiceListAPIView,
    InvoiceCUDAPIView,
    ProjectCUDAPIView,
    MeetingListAPIView,
    MeetingCUDAPIView,
    ProjectListAPI,
    

) 


from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.BASE.views import get_upload_api_view




app_name = "cms"
API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register('client/list',ClientListAPIView,basename="client-list")
router.register('client/cud',ClientCUDAPIView,basename="client-cud")

router.register('invoice/list',InvoiceListAPIView,basename="invoice-list")
router.register('invoice/cud',InvoiceCUDAPIView,basename="invoice-cud")


router.register('project/cud',ProjectCUDAPIView,basename="project-cud")

router.register('meeting/list',MeetingListAPIView,basename="meeting-list")
router.register('meeting/cud',MeetingCUDAPIView,basename="meeting-cud")

urlpatterns = [
    path('project/list/<uuid>/', ProjectListAPI.as_view({'get': 'list'}), name='project-list'),
    path('document/file/',get_upload_api_view(meta_model=DocumentFile).as_view())
] + router.urls
