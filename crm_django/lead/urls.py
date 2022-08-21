from django.urls import path,include

from rest_framework.routers import DefaultRouter

from lead.api import views as lv 

router = DefaultRouter()
router.register(r'leads', lv.LeadViewSet,basename='Lead')

urlpatterns = [
    path('', include(router.urls))
]


