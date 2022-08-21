from django.conf import settings
from django.db import models
from core.models import TimeStamp


class Team(TimeStamp):
    name = models.CharField(max_length=255) #team name
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name