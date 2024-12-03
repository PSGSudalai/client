from django.urls import path, re_path
from apps.ACCESS.views import LoginView, LogoutView, GetAuthUserDetails, RegisterView
from apps.ACCESS.views.chatroom import ChatRoomViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "access"
API_URL_PREFIX = "api/"


router = SimpleRouter()
router.register('chatrooms', ChatRoomViewSet, basename='chatroom')
router.register('messages', MessageViewSet, basename='message')



urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/details/", GetAuthUserDetails.as_view(), name="login"),
] + router.urls

