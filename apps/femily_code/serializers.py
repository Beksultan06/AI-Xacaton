from rest_framework import serializers
from .models import Family

# Сериализатор для создания семьи
class FamilyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['code']

    def create(self, validated_data):
        user = self.context['request'].user
        family = Family.objects.create(created_by=user, **validated_data)
        family.members.add(user)  # Добавляем создателя в семью автоматически
        return family


# Сериализатор для присоединения к семье
class FamilyJoinSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)

    def validate_code(self, value):
        try:
            self.family = Family.objects.get(code=value)
        except Family.DoesNotExist:
            raise serializers.ValidationError("Семья с указанным кодом не найдена.")
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        self.family.members.add(user)  # Добавляем пользователя в семью
        return self.family
