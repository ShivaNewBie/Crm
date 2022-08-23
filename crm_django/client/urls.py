from django.urls import path,include

from rest_framework.routers import DefaultRouter

from client.api.views import ClientViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet,basename='Client')
router.register(r'notes', NoteViewSet,basename='Note')

urlpatterns = [
    path('', include(router.urls))
]


