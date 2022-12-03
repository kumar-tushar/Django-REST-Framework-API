from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
