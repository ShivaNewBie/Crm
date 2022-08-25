from django.urls import path,include

from rest_framework.routers import DefaultRouter


from team.api.views import get_my_team,add_member, UserDetail,upgrade_plan,get_stripe_pub_key, create_checkout_session,stripe_webhook, check_session


from team.api import views as tv

router = DefaultRouter()
router.register(r'teams', tv.TeamViewSet,basename='Team')

urlpatterns = [
    path('teams/member/<int:pk>/',UserDetail.as_view(), name='user_detail'),

    path('teams/get_my_team/',get_my_team, name='get_my_team'),
    path('teams/add_member/',add_member, name='add_member'),
    path('teams/upgrade_plan/',upgrade_plan, name='upgrade_plan'),

    path('stripe/get_stripe_pub_key/',get_stripe_pub_key, name='get_stripe_pub_key'),
    path('stripe/create_checkout_session/',create_checkout_session, name='create_checkout_session'),
    path('stripe/webhook/',stripe_webhook, name='stripe_webhook'),
    path('stripe/check_session/',check_session, name='check_session'),

    path('', include(router.urls)),
]