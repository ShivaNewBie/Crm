from django.conf import settings
from django.db import models
from core.models import TimeStamp


class Plan(models.Model):
    plan_name = models.CharField(max_length=255)
    max_leads = models.IntegerField(default=5)
    max_clients = models.IntegerField(default=5)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.plan_name


class Team(TimeStamp):
    team_name = models.CharField(max_length=255)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.SET_NULL, null=True,blank=True )


    def __str__(self):
        return self.team_name