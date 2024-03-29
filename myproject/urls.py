from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
