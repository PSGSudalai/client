from apps.ADMIN.models import Document,Project
from apps.BASE.serializers import ReadOnlySerializer, read_serializer


class DocumentReadSerializer(ReadOnlySerializer):
    project_detail = read_serializer(meta_model=Project,meta_fields=["id","uuid","title","status","amount"])(source="project")
    class Meta(ReadOnlySerializer.Meta):
        model = Document
        field = [
            "id",
            "uuid",
            "doc_id",
            "project_detail",
            "date"
        ]


class QuotationReadSerializer(ReadOnlySerializer):
    project_detail = read_serializer(meta_model=Project,meta_fields=["id","uuid","title","status","amount"])(source="project")
    class Meta(ReadOnlySerializer.Meta):
        model = Document
        field = [
            "id",
            "uuid",
            "qua_id",
            "project_detail",
            "date"
        ]


