
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Contact
# from .serializers import ContactSerializer


# @api_view(['GET'])
# def contact_list(request):
#     """
#     List all code contacts, or delete a  contact.
#     """
#     if request.method == 'GET':
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'DELETE'])
# def detail_contact(request, id):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         contact = Contact.objects.get(pk=id)
#     except Contact.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response(status=status.HTTP_204_NO_CONTENT)
