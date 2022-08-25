from rest_framework import viewsets,filters
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination

from django.http import Http404


from team.models import Team
from lead.models import Lead


from client.api.serializers import ClientSerializer, NoteSerializer
from client.models import Client, Note

class ClientPagination(PageNumberPagination):
    page_size = 10


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,) #we get &search in leads frontend
    search_fields = ('name', 'contact_person')

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

@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try: 
        lead = Lead.objects.filter(associated_team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404 

    client = Client.objects.create(associated_team=team, name=lead.company_name, 
                                    contact_person=lead.contact_person, 
                                    email=lead.email, 
                                    phone=lead.phone,website=lead.website, created_by=request.user)
    return Response()