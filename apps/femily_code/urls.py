from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FamilyViewSet

router = DefaultRouter()
router.register('family', FamilyViewSet, basename='family')

urlpatterns = [
    path('', include(router.urls)),  # Включает маршруты, созданные роутером
    path('family/join/', FamilyViewSet.as_view({'post': 'join'}), name='family-join'),
    path('family/retrieve-by-token/', FamilyViewSet.as_view({'get': 'retrieve_by_token'}), name='family-by-token'),
]
