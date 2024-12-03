from apps.ADMIN.models import Project,Client
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer




    

class ProjectReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = Project
        fields = [
            "id",
            "project_name",
            "team_leader",
            "task_no",
            "total_budget",
            "start_date",
            "deadline",
            "description",
        ]


class ProjectWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model=Project
        fields = [
            "client",
            "project_name",
            # "team_leader",
            # "task_no",
            # "total_budget",
            # "start_date",
            # "deadline",
            "description",
        ]
        