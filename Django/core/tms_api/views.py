# Create your views here.
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly
from tms.models import Request

from .serializers import RequestSerializer


class PostUserWritePermission(BasePermission):
    message = 'Editing request is restricted to the owner only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


class RequestList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
