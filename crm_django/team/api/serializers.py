from rest_framework import serializers

from user.serializers import UserSerializer
from team.models import Team, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan 
        fields = (
            '__all__'
        )
class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = Team 
        fields = ('id','team_name','members','created_by','plan','plan_end_date')


