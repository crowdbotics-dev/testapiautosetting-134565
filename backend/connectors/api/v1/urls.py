from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134565ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134565", Testconnectors134565ViewSet, basename="testconnectors134565"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
