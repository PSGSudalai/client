from apps.ADMIN.models import Meeting
from apps.ADMIN.serializers import MeetingReadSerializer, MeetingWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet


class MeetingListAPIView(ListAPIViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingReadSerializer

    all_table_columns={
        "client.name":"Client Name",
        "project.project_name":"Project Name",
        "description":"Description",
        "date":"Date",
        "team":"Team",
        "start_time":"Time",
        "status":"Status"
    }

    def get_meta_for_table(self):
        data={
            "column":self.all_table_columns
        }
        return data

class MeetingCUDAPIView(CUDAPIViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingWriteSerializer