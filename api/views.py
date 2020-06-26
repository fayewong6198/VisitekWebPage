
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from knox.models import AuthToken

from blogs.models import Blog
from blogs.serializers import BlogSerializer
from contact.models import Contact
from contact.serializers import ContactSerializer
from accounts.models import User
from accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer


@api_view(['GET', "POST", ])
def blog_list(request):
    """
    List all code contacts, or delete a  contact.
    """
    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response({'message': 'Blog were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

##########################################################################################################################
@api_view(['GET'])
def contact_list(request):
    """
    List all code contacts, or delete a  contact.
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def detail_contact(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

# ########################################################################################################################


class Login(generics.GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() == False:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class Register(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() == False:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


@api_view(['GET'])
def get_users(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.user.is_authenticated:

        if request.method == 'GET':

            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    return Response({'msg': "login required"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        request.data['password'] = hashlib.sha256(
            str(request.data['password']).encode()).hexdigest()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({'mgs': "success"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
