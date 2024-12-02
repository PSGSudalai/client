from apps.ADMIN.models import Project,Client
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer


class ProjectReadSerializer(ReadOnlySerializer):
    client_detail =read_serializer(Client,meta_fields=["id","uuid","project_name"])(source="project_client")
    class Meta(ReadOnlySerializer.Meta):
        model = Project
        fields = [
            "id",
            "uuid",
            "client_detail",
            "project_name",
            "team_leader",
            "task_no",
            "total_budget",
            "start_date",
            "deadline",
            "description"
        ]


class ProjectWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Project
        fields = [
            "project_client",
            "project_name",
            "team_leader",
            "task_no",
            "total_budget",
            "start_date",
            "deadline",
            "description"
        ]
    