from django.urls import path
from rest_framework.routers import DefaultRouter

from dlrApp.view.controller import ClientViewSet

router = DefaultRouter()


urlpatterns = [
    path(
        "duplicateClinet/",
        ClientViewSet.as_view(
            {
                "post": "create",
            }
        ),
        name="client",
    ),
]
