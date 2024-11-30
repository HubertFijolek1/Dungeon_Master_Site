from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from rest_framework import viewsets, permissions
from .models import Message, ForumPost, Poll, PollOption, PollVote
from .serializers import (
    MessageSerializer, ForumPostSerializer, PollSerializer, PollVoteSerializer
)
from .forms import MessageForm, ForumPostForm, PollForm, PollOptionFormSet
from django.contrib.auth import get_user_model

User = get_user_model()

# Permissions

class IsParticipant(permissions.BasePermission):
    """
    Custom permission to only allow sender or receiver to access the message.
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors to edit or delete their own posts.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# API ViewSets

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsParticipant]

    def get_queryset(self):
        return Message.objects.filter(
            Q(sender=self.request.user) | Q(receiver=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

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

class PollVoteViewSet(viewsets.ModelViewSet):
    queryset = PollVote.objects.all()
    serializer_class = PollVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PollVote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Django Views

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
            Q(sender=self.request.user) | Q(receiver=self.request.user)
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

class PollListView(ListView):
    model = Poll
    template_name = 'interactions/poll_list.html'
    context_object_name = 'polls'

class PollDetailView(DetailView):
    model = Poll
    template_name = 'interactions/poll_detail.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_vote = None
        if self.request.user.is_authenticated:
            user_vote = PollVote.objects.filter(user=self.request.user, poll=self.object).first()
        context['user_vote'] = user_vote
        return context

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'interactions/poll_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = PollOptionFormSet(self.request.POST)
        else:
            data['formset'] = PollOptionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

def vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        if option_id:
            selected_option = get_object_or_404(PollOption, id=option_id, poll=poll)
            if not PollVote.objects.filter(user=request.user, poll=poll).exists():
                PollVote.objects.create(user=request.user, poll=poll, selected_option=selected_option)
        return redirect('interactions:poll_detail', pk=poll_id)

def chat_view(request):
    return render(request, 'interactions/chat.html')