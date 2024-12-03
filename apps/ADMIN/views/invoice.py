from apps.ADMIN.serializers import InvoiceReadSerializer, InvoiceWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Invoice

class InvoiceListAPIView(ListAPIViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceReadSerializer

    all_table_columns ={
        "invoice_id":"Invoice ID",
        "client_name.name":"Client Name",
        "project.project_name":"Project Name",
        "total":"Price",
        "created":"Date"
    }

    def get_meta_for_table(self):
        data={
            "column":self.all_table_columns
        }
        return data
    
class InvoiceCUDAPIView(CUDAPIViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceWriteSerializer
    