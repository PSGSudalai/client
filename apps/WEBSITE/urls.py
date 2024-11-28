from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.ADMIN.models import ProjectImage
from apps.BASE.views import get_upload_api_view
from apps.WEBSITE.views import (
        ProjectListAPIView,
        FeedbackListAPIView,
        FeedbackCUDAPIView,
) 

app_name = "web"
API_URL_PREFIX = "api/"


router = SimpleRouter()

router.register('project/list',ProjectListAPIView,basename="project-list")
router.register('feedback/list',FeedbackListAPIView,basename="feedback-list")
urlpatterns = [
    path("project/image/",get_upload_api_view(meta_model=ProjectImage).as_view()),
    path("feedback/cud/",FeedbackCUDAPIView.as_view()),
] + router.urls
