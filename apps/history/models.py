from django.db import models
from apps.users.models import User
from apps.history.constant import TIME_CHOICE

class Daily(models.Model):
    DAILY = 'daily'
   

    SCHEDULE_TYPES = [
        (DAILY, 'Daily'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    

class Weekly(models.Model):
    Weekly = 'weekly'
   

    SCHEDULE_TYPES = [
        (Weekly, 'Weekly'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weekly')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class History(models.Model):
    title_day = models.ForeignKey(Daily, on_delete=models.CASCADE, related_name="ежедневно")
    title_week = models.ForeignKey(Weekly, on_delete=models.CASCADE, related_name="еженедельно")
    time_choice = models.CharField (max_length=50, choices=TIME_CHOICE)

    def __str__(self):
        return f"{self.title_day} "
    
