from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.history.paginations import HistoryPagination
from .models import Daily, Weekly, History
from .serializers import WeeklySerializer, DailySerializer, HistorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class WeeklyViewSet(viewsets.ModelViewSet):
    queryset = Weekly.objects.all()
    serializer_class = WeeklySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['time_choice']
    pagination_class = HistoryPagination