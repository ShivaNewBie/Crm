from django.db import models
from django.conf import settings

from core.models import TimeStamp

from team.models import Team

class Lead(TimeStamp):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED,'Contacted'),
        (INPROGRESS, 'Inprogress'),
        (LOST, 'Lost'),
        (WON, 'Won')
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )

    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True,null=True) #how sure we can get this lead
    estimated_value = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=255, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=255, choices=CHOICES_PRIORITY, default=MEDIUM)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='asigned_leads',on_delete=models.SET_NULL, null=True,blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    associated_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='leads')
