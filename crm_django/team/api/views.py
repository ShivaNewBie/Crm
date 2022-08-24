from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404

from team.models import Team
from team.api.serializers import TeamSerializer, UserSerializer

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

class UserDetail(APIView):
    def get_object(self, pk):
        try: 
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self,request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
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

