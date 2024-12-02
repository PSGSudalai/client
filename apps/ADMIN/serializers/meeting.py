from apps.ADMIN.models import Project
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer
from apps.ADMIN.models import Meeting;



class MeetingReadSerializer(ReadOnlySerializer):
    project = read_serializer(Project,meta_fields=["id","uuid","project_name"])(source="project_meeting")
    class Meta(ReadOnlySerializer.Meta):
        model= Meeting
        fields = [
            "id",
            "uuid",
            "project",
            "title",
            "date",
            "start_time",
            "end_time",
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
            "title",
            "date",
            "start_time",
            "end_time",
            "team",
            "link",
            "status",
            "description"
            
        ]