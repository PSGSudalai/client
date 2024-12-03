from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer
from apps.ADMIN.models import Document


class DocumentWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Document
        fields = [
            "image"
            
        ]


class DocumentReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = Document
        fields = [
            "id",
            "uuid",
            "image_detail",
            "feedback_detail",
            ""
        ]