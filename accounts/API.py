
# import hashlib
# from .models import User
# from rest_framework import status
# from .serializers import UserSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import jwt
# from datetime import datetime, timedelta

# # def get_permissions(self):
# #     permission_classes = []
# #     if self.action == 'create':
# #         permission_classes = [AllowAny]
# #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
# #         permission_classes = [IsLoggedInUserOrAdmin]
# #     elif self.action == 'list' or self.action == 'destroy':
# #         permission_classes = [IsAdminUser]
# #     return [permission() for permission in permission_classes]


# @api_view(['POST'])
# def login(request):
#     try:
#         user = User.objects.get(username=request.data['username'])
#         # x = sha256(as_bytestring(user.password)).hexdigest().decode('ascii')
#         print('-----3------', x)
#         key = 'secret'
#         payload = {
#             'user_username': user.username,
#         }
#         print('-----3------')
#         jwt_token = jwt.encode(payload, key, 'HS256')
#         return Response({'token': jwt_token})
#     except (User.DoesNotExist, User.PasswordDoesNotMatch):
#         return Response({'message': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def get_users(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         request.data['password'] = hashlib.sha256(
#             str(request.data['password']).encode()).hexdigest()
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         request.data['password'] = hashlib.sha256(
#             str(request.data['password']).encode()).hexdigest()
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         return Response({'mgs': "success"}, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
