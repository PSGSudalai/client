


from apps.ADMIN.models.invoice import Invoice
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer
from rest_framework import serializers

class InvoiceReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = Invoice
        fields = [
            "id",
            "uuid",
            "invoice_id",
            "project_name", 
            "client_name",
            "phone",
            "client_address",
            "amount_description",
            "sub_total",
            "tax",
            "total"
        ]

 
        

class InvoiceWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Invoice
        fields = [
            "client_name",
            "phone",
            "client_address",
            "amount_description",
            "sub_total",
            "tax",
            "total"
        ]


    