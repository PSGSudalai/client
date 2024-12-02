from apps.ADMIN.models import Client
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer


class ClientReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = Client
        fields = [
            "id",
            "uuid",
            "name",
            "project_name",
            "email",
            "contact",
            "description"
        ]


class ClientWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Client
        fields = [
            "name",
            "project_name",
            "email",
            "contact",
            "description"
        ]