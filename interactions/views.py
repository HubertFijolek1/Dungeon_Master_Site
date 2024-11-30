from rest_framework import viewsets, permissions
from .models import Message, ForumPost, Poll, PollVote, PollOption
from .serializers import MessageSerializer, ForumPostSerializer, PollSerializer, PollVoteSerializer
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .forms import MessageForm, ForumPostForm, PollForm

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

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'interactions/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'interactions/message_detail.html'
    context_object_name = 'message'

    def get_queryset(self):
        return Message.objects.filter(
            (Q(sender=self.request.user) | Q(receiver=self.request.user))
        )

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'interactions/message_form.html'
    success_url = reverse_lazy('interactions:message_list')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class ForumPostListView(ListView):
    model = ForumPost
    template_name = 'interactions/forum_post_list.html'
    context_object_name = 'forum_posts'

class ForumPostDetailView(DetailView):
    model = ForumPost
    template_name = 'interactions/forum_post_detail.html'
    context_object_name = 'forum_post'

class ForumPostCreateView(LoginRequiredMixin, CreateView):
    model = ForumPost
    form_class = ForumPostForm
    template_name = 'interactions/forum_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

lass PollListView(ListView):
    model = Poll
    template_name = 'interactions/poll_list.html'
    context_object_name = 'polls'

class PollDetailView(DetailView):
    model = Poll
    template_name = 'interactions/poll_detail.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_vote = PollVote.objects.filter(user=self.request.user, poll=self.object).first()
        context['user_vote'] = user_vote
        return context

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'interactions/poll_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

def vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        if option_id:
            selected_option = get_object_or_404(PollOption, id=option_id, poll=poll)
            if not PollVote.objects.filter(user=request.user, poll=poll).exists():
                PollVote.objects.create(user=request.user, poll=poll, selected_option=selected_option)
        return redirect('interactions:poll_detail', pk=poll_id)