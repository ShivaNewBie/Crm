

from rest_framework import viewsets

from lead.models import Lead

from lead.api.serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    
    def get_queryset(self):
        created_by = self.request.user 
        return Lead.objects.filter(created_by=created_by)
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)
        