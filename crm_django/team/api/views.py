from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from team.models import Team
from team.api.serializers import TeamSerializer

from user.models import CustomUser

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    def get_queryset(self):
        # return Team.objects.filter(members__in=[self.request.user])
        return self.queryset.filter(members=self.request.user)
    def perform_create(self,serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user) #user who created will be member of team 
        obj.save()

@api_view(['GET'])

def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    print(request.user)

    return Response(serializer.data)

@api_view(['POST'])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    email = request.data['email']

    print('Email', email)

    user = CustomUser.objects.get(email=email)

    team.members.add(user)
    team.save()

    return Response()

# class MyTeamAPIView(generics.ListAPIView):
#     serializer_class = TeamSerializer

