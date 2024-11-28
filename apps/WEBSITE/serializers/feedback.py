from apps.ADMIN.models import Document,Feedback
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer


class FeedbackReadSerializer(ReadOnlySerializer):
    document_detail = read_serializer(meta_model=Document,meta_fields=["id","uuid","doc_id"])(source="document")
    class Meta(ReadOnlySerializer.Meta):
        model = Feedback
        fields =[
            "id",
            "uuid",
            "document_detail",
            "description"
        ]
