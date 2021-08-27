from django.shortcuts import redirect, render
from django.urls import reverse

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from comment.api.models import Comment
from .serializer import CommentSerializer
from custom_user.permission import IsOwner

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer


class UpDelComment(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    queryset = Comment.objects.all()
    model = Comment

    def get_permissions(self):
        method = self.request.method
        if method == 'PUT' or method == 'PATCH' or method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()
    
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        kwargs.pop('comment_id')
        return redirect(reverse('comment_list',kwargs=kwargs))


class ListComment(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(level=1)


class ListSubComment(ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        post = self.kwargs['post_id']
        parent = self.kwargs['comment_id']
        return Comment.objects.filter(parent=parent, post=post)
