from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from .permission import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_permissions(self):
    permission_classes = []
    if self.action == 'create':
        permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
        permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]


@api_view(['GET', 'POST'])
def users(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = User(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = User(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
