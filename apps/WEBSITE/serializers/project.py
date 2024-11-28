from apps.ADMIN.models import Project,ProjectImage
from apps.BASE.serializers import ReadOnlySerializer, read_serializer


class ProjectReadSerializer(ReadOnlySerializer):
    image_detail = read_serializer(meta_model=ProjectImage,meta_fields=["id","uuid","file"])(source="image")
    class Meta(ReadOnlySerializer.Meta):
        model = Project
        fields = [
            "id",
            "uuid",
            "title",
            "image_detail",
            "start_date",
            "end_date",
            "status",
            "amount"
        ]