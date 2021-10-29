
# Create your views here.
from todo_app.models import Note
from todo_app.serializers import NoteSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions
from todo_app.permissions import IsOwner

User = get_user_model()
 

class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    def get_queryset(self):
        return Note.objects.filter(created_by=self.request.user.pk)
        


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
