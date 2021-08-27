from django.shortcuts import render
from django.db.models import Q

from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializer import CreatePostSerializer, UpDelPostSerializer, DetailPostSerializer, LikeSerializer
from .models import Post
from ..permission import ObjectIsAccessible
from custom_user.permission import IsOwner


class CreatePost(CreateAPIView):
    serializer_class = CreatePostSerializer


class PostViewSet(ModelViewSet):
    lookup_url_kwarg = 'post_id'
    model = Post

    def get_queryset(self):
        user = self.request.user
        method = self.request.method
        if method == 'PUT' or method == 'PATCH' or method == 'DELETE':
            if user.is_superuser:
                return Post.objects.filter()
            return user.post_owner.all()
        elif method == 'GET':
            return Post.objects.filter(Q(mode='PB') | Q(user=user))
        else:
            raise MethodNotAllowed(method=method)

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'PATCH' or method == 'DELETE':
            return UpDelPostSerializer
        elif method == 'GET':
            return DetailPostSerializer
        else:
            raise MethodNotAllowed(method=method)

    def get_permissions(self):
        method = self.request.method
        isowner_method = ['PATCH', 'PUT', 'DELETE']
        if method in isowner_method:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


class LikeViewSet(ModelViewSet):
    lookup_url_kwarg = 'post_id'
    model = Post
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, ObjectIsAccessible]

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs['post_id'])

    def perform_destroy(self, instance):
        user = self.request.user
        if user in instance.like.all():
            instance.like.remove(user)

    def create(self, request, *args, **kwargs):
        obj = self.get_object()
        self.check_object_permissions(request, obj)
        return super().create(request, *args, **kwargs)
