
from apps.ADMIN.serializers import ProjectWriteSerializer,ProjectReadSerializer
from apps.BASE.views import CUDAPIViewSet,AppAPIView, ListAPIViewSet
from apps.ADMIN.models import Project, Client





class ProjectListAPI(ListAPIViewSet):
    serializer_class=ProjectReadSerializer
    def get_queryset(self):
        uuid=self.kwargs["uuid"]
        client = Client.objects.get(uuid=uuid)
        return Project.objects.filter(client=client)
   
    


class ProjectCUDAPIView(CUDAPIViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectWriteSerializer