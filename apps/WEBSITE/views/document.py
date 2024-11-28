from apps.ADMIN.models import Document
from apps.BASE.views import ListAPIViewSet
from apps.WEBSITE.serializers import DocumentReadSerializer
from apps.WEBSITE.serializers.document import QuotationReadSerializer


class DocumentListAPIView(ListAPIViewSet):
    serializer_class = DocumentReadSerializer
    def get_queryset(self):
        user = self.get_authenticated_user
        return Document.objects.filter(user=user)


class QuotationListAPIView(ListAPIViewSet):
    def get_queryset(self):
        user = self.get_authenticated_user
        return Document.objects.filter(user=user)
    serializer_class = QuotationReadSerializer