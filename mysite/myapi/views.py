from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('title')
    serializer_class = NoteSerializer