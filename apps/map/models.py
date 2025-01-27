from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forparents")
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    waypoints = models.JSONField(blank=True, null=True)  # Промежуточные точки
    comment = models.TextField(blank=True, null=True)
    additional_points = models.JSONField(blank=True, null=True, verbose_name="Дополнительные пути")  # Дополнительные точки маршрута
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location} by {self.user.username}"


class Route2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forkids")
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    waypoints = models.JSONField(blank=True, null=True, verbose_name="Промежуточные точки")  # Промежуточные точки
    schedule = models.JSONField(blank=True, null=True, verbose_name="График дня")  # График дня, если нужно
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location} by {self.user.username}"


