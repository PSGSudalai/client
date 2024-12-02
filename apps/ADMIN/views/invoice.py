from apps.ADMIN.serializers import InvoiceReadSerializer, InvoiceWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Invoice

class InvoiceListAPIView(ListAPIViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer

    
class InvoiceCUDAPIView(CUDAPIViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceWriteSerializer
    