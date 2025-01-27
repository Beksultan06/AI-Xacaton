from rest_framework import serializers
from .models import Daily, Weekly, History

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = ['id', 'title', 'description',  'user', 'date']

class WeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekly
        fields = ['id', 'title', 'description',  'user', 'date']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['title_day', 'title_week', 'time_choice']