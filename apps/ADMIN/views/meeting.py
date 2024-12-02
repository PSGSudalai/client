from apps.ADMIN.models import Meeting
from apps.ADMIN.serializers import MeetingReadSerializer, MeetingWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet


class MeetingListAPIview(ListAPIViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingReadSerializer

class MeetingCUDAPIview(CUDAPIViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingWriteSerializer