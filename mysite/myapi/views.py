from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .models import Note

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('title')
    serializer_class = NoteSerializer

class NoteApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    #function to get all notes
    def get(self, request, *args, **kwargs):
        
     notes = Note.objects.all().order_by('title')
     serializer = NoteSerializer(notes, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)

#function to create a new note
    def post(self, request, *args, **kwargs):
     
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'id':request.data.get('id')
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)