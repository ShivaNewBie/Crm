
from rest_framework import viewsets,filters
from user.models import CustomUser

from rest_framework.pagination import PageNumberPagination


from lead.api.serializers import LeadSerializer

from lead.models import Lead 

from team.models import Team


class LeadPagination(PageNumberPagination):
    page_size = 10



class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,) #we get &search in leads frontend
    search_fields = ('company_name', 'contact_person')

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
        