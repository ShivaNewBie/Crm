from django.db import models
from django.conf import settings

from core.models import TimeStamp

from team.models import Team

class Client(TimeStamp):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients')
    associated_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='clients')

class Note(TimeStamp):
    associated_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='notes')
    client = models.ForeignKey(Client,on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
