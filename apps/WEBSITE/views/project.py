from apps.ADMIN.models import Project
from apps.BASE.views import ListAPIViewSet
from apps.WEBSITE.serializers import ProjectReadSerializer


class ProjectListAPIView(ListAPIViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectReadSerializer