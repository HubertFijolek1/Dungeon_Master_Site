from rest_framework import viewsets, permissions
from .models import Message, ForumPost, Poll, PollVote
from .serializers import MessageSerializer, ForumPostSerializer, PollSerializer, PollVoteSerializer

class IsParticipant(permissions.BasePermission):
    """
    Custom permission to only allow sender or receiver to access the message.
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsParticipant]

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors to edit or delete their own posts.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the post.
        return obj.author == request.user

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class PollVoteViewSet(viewsets.ModelViewSet):
    queryset = PollVote.objects.all()
    serializer_class = PollVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PollVote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)