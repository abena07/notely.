from django.shortcuts import render,get_object_or_404,redirect
from rest_framework import viewsets
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .models import Note
from .forms import NoteForm

# Create your views here.
"""class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('title')
    serializer_class = NoteSerializer"""

"""class NoteApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    #function to get all notes
    def get(self, request, *args, **kwargs ):
        
     notes = Note.objects.all().order_by('id')
     serializer = NoteSerializer(notes, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)
     

    #function to create a new note
    def note(self, request, *args, **kwargs):
     
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'id':request.data.get('id')
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        '''
        Helper method to get the object with given id, 
        '''
        try:
            return Note.objects.get(id=id)
        except Note.DoesNotExist:
            return None
    
    def get(self, request, id, *args, **kwargs):
        '''
        Retrieves the note with given note_id
        '''
        note_instance = self.get_object(id)
        if not note_instance:
            return Response(
                {"res": "Object with note id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NoteSerializer(note_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 4. Update
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the note item with given note_id if exists
        '''
        note_instance = self.get_object(id)
        if not note_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'id':request.data.get('id')
        }
        serializer =    NoteSerializer(instance = note_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 5. Delete
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the note item with given id if exists
        '''
        note_instance = self.get_object(id)
        if not note_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        note_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )"""


#actual views for my files
def note_list(request):
    notes = Note.objects.all().order_by('id')
    return render(request, 'note/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/note_detail.html', {'note': note})

def note_new(request):
    form = NoteForm()
    return render(request, 'note/note_edit.html', {'form': form})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note/note_edit.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/note_edit.html', {'form': form})