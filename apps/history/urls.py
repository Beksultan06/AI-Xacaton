from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyViewSet, WeeklyViewSet, HistoryViewSet

router = DefaultRouter()
router.register(r'daily', DailyViewSet)
router.register(r'weekly', WeeklyViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
