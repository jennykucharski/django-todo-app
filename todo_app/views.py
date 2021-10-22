
# Create your views here.
from todo_app.models import Note
from todo_app.serializers import NoteSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()
 
 
class NoteList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
