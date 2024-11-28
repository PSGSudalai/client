from apps.ADMIN.models.feedback import Feedback
from apps.BASE.base import AppAPIView
from apps.BASE.views import ListAPIViewSet
from apps.BASE.views.generic import CUDAPIViewSet
from apps.WEBSITE.serializers.feedback import FeedbackReadSerializer


class FeedbackListAPIView(ListAPIViewSet):
    serializer_class = FeedbackReadSerializer
    def get_queryset(self):
        user = self.get_authenticated_user()
        return Feedback.objects.filter(user=user)
    
class FeedbackCUDAPIView(AppAPIView):
    def post(self, request, *args, **kwargs):
        user = self.get_authenticated_user() 
        if not user:
            return self.send_error_response("User not authenticated")
        document = request.POST.get("document")
        description = request.POST.get("description")
        if not document or not description:
            return self.send_error_response("Document and description fields are required")

        # Create the feedback instance
        feedback = Feedback.objects.create(
            document=document,
            description=description
        )

        return self.send_response(data={"feedback_id": feedback.id}, message="Feedback created successfully")
