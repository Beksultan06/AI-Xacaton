from rest_framework import serializers

from apps.users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ('id_passport','username' ,'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        # Валидация пароля
        if len(attrs['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий')
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Пароли отличаются")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')

        user = User.objects.create(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            last_name=validated_data['last_name'],
            id_passport=validated_data['id_passport'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user