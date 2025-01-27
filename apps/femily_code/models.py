from django.db import models
from django.conf import settings

# Модель для семьи
class Family(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Код семьи
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="created_families"
    )  # Создатель семьи
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="families",
        blank=True
    )  # Члены семьи

    def __str__(self):
        return self.code
