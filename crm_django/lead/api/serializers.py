from rest_framework import serializers

from lead.models import Lead

from user.serializers import UserSerializer



class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Lead
        exclude = ( #exclude associated team 
            'associated_team',
        )  
    
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')
    def get_updated_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')