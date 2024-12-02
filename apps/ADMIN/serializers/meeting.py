from apps.ADMIN.models import Project,Meeting,Client
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer




class MeetingReadSerializer(ReadOnlySerializer):
    project = read_serializer(Project,meta_fields=["id","uuid","project_name"])(source="project_meeting")
    client = read_serializer(Client,meta_fields=["id","uuid","name"])(source="client_name")
    class Meta(ReadOnlySerializer.Meta):
        model= Meeting
        fields = [
            "id",
            "uuid",
            "project",
            "client",
            "title",
            "date",
            "start_time",
            "team",
            "link",
            "status",
            "description"
        ]


class MeetingWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Meeting
        fields = [
            "project_meeting",
            "client_name",
            "title",
            "date",
            "start_time",
            "team",
            "link",
            "status",
            "description"
            
        ]