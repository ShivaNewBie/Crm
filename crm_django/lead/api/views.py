
from rest_framework import viewsets
from user.models import CustomUser

from lead.api.serializers import LeadSerializer

from lead.models import Lead 

from team.models import Team

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first() #members will be able to see leads not just the owner   
        return self.queryset.filter(associated_team=team)

    
    def perform_update(self,serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']

        if member_id:
            user = CustomUser.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()

    def perform_create(self,serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(associated_team=team,created_by=self.request.user)
        