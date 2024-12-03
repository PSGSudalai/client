
from apps.ADMIN.models import Invoice,Project,Client
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer
from rest_framework import serializers

class InvoiceReadSerializer(ReadOnlySerializer):
    project_detail = read_serializer(Project,meta_fields=["id","uuid","project_name"])(source="project")
    client_detail = read_serializer(Client,meta_fields=["id","uuid","name"])(source="client_name")
    class Meta(ReadOnlySerializer.Meta):
        model = Invoice
        fields = [
            "id",
            "uuid",
            "invoice_id",
            "project_detail", 
            "client_detail",
            "phone",
            "client_address",
            "amount_description",
            "sub_total",
            "tax",
            "total",
            "created"
        ]

 
        

class InvoiceWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Invoice
        fields = [
            "client_name",
            "project",
            "phone",
            "client_address",
            "amount_description",
            "sub_total",
            "tax",
            "total"
        ]


    