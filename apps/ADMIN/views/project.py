from apps.ADMIN.serializers import ProjectReadSerializer,ProjectWriteSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Project

class ProjectListAPIView(ListAPIViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectReadSerializer

class ProjectCUDAPIView(CUDAPIViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectWriteSerializer
    