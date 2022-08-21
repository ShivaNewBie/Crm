from rest_framework import serializers

from user.serializers import UserSerializer
from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Team 
        fields = ('id','name','members','created_by')