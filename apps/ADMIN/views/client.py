from apps.ADMIN.serializers import ClientReadSerializer,ClientWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Client

class ClientListAPIView(ListAPIViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientReadSerializer



class ClientCUDAPIView(CUDAPIViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientWriteSerializer
