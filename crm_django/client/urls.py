from django.urls import path,include

from rest_framework.routers import DefaultRouter

from client.api.views import ClientViewSet, NoteViewSet, convert_lead_to_client

router = DefaultRouter()
router.register(r'clients', ClientViewSet,basename='Client')
router.register(r'notes', NoteViewSet,basename='Note')

urlpatterns = [
    path('convert_lead_to_client/',convert_lead_to_client, name='convert-lead-to-client'),

    path('', include(router.urls))
]


