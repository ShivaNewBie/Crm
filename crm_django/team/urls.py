from django.urls import path,include

from rest_framework.routers import DefaultRouter


from team.api.views import get_my_team,add_member


from team.api import views as tv

router = DefaultRouter()
router.register(r'teams', tv.TeamViewSet,basename='Team')

urlpatterns = [
    path('teams/get_my_team/',get_my_team, name='get_my_team'),
    path('teams/add_member/',add_member, name='add_member'),


    path('', include(router.urls)),
]