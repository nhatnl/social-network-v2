
from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView

from .serializer import UserSerializer
from .models import CustomUser


class CurrentUserDetail(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class DetailUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter()
    lookup_url_kwarg = 'user_id'


class ListUser(ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return CustomUser.objects.exclude(id = self.request.user.id)
