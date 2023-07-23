from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PawnPositionsViewSet


router = DefaultRouter(trailing_slash=False)
router.register('', viewset=PawnPositionsViewSet, basename='pawn-positions')


urlpatterns = [
    path('', include(router.urls))
]
