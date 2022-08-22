from rest_framework import serializers

from lead.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Lead
        exclude = (
            'associated_team',
        )
    
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')
    def get_updated_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')