from rest_framework import serializers

from client.models import Client,Note

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Client
        exclude = ( #exclude associated team 
            'associated_team',
        )  
    
    def get_created_at(self,instance): #modified date time
        return instance.created_at.strftime('%B, %d, %Y')
    def get_updated_at(self,instance): #modified date time
        return instance.updated_at.strftime('%B, %d, %Y')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note 
        fields = (
            'id', 'name', 'body',
        )