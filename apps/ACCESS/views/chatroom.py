from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.ACCESS.models.chatroom import ChatRoom, Message
from apps.ACCESS.serializers.chatroom import ChatRoomSerializer, MessageSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        return self.request.user.chatrooms.all()

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        chatroom = self.get_object()
        if request.user not in chatroom.users.all():
            return Response({'error': 'Access denied'}, status=403)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chatroom=chatroom, sender=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chatroom_id = self.request.query_params.get('chatroom_id')
        if chatroom_id:
            return Message.objects.filter(chatroom_id=chatroom_id)
        return Message.objects.none()
