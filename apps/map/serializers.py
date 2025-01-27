from rest_framework import serializers
from .models import Route, Route2

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['start_location', 'end_location', 'waypoints', 'comment', 'additional_points', 'updated_at' ]
        
class Route2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Route2
        fields = ['id', 'user', 'start_location', 'end_location', 'waypoints', 'comment', 'schedule', 'created_at', 'updated_at']
