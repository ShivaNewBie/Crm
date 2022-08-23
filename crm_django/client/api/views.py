
from rest_framework import viewsets

from client.api.serializers import ClientSerializer, NoteSerializer
from client.models import Client, Note

from team.models import Team

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first() #members will be able to see leads not just the owner   
        return self.queryset.filter(associated_team=team)

    
    def perform_create(self,serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(associated_team=team,created_by=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first() #members will be able to see leads not just the owner   
        client_id = self.request.GET.get('client_id') #reference to client field in note model

        return self.queryset.filter(associated_team=team).filter(client_id=client_id)
    
    def perform_create(self,serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id'] #reference to client field in note model

        serializer.save(associated_team=team,created_by=self.request.user, client_id=client_id)