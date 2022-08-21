from django.urls import path,include

from rest_framework.routers import DefaultRouter


from team.api.views import get_my_team


from team.api import views as tv

router = DefaultRouter()
router.register(r'teams', tv.TeamViewSet,basename='Team')

urlpatterns = [
    path('teams/get_my_team/',get_my_team, name='get_my_team'),


    path('', include(router.urls)),
]