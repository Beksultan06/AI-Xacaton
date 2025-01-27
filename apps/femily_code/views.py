from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, permissions
from .models import Family
from .serializers import FamilyCreateSerializer, FamilyJoinSerializer
import jwt

# Вьюсет для работы с семьями
class FamilyViewSet(viewsets.ViewSet):
    # permission_classes = [permissions.IsAuthenticated]

    # Создание семьи
    def create(self, request):  
        serializer = FamilyCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            family = serializer.save()
            return Response({"message": "Семья успешно создана!", "family_code": family.code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Подключение к семье
    @action(detail=False, methods=['post'])
    def join(self, request):
        serializer = FamilyJoinSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            family = serializer.save()
            return Response({"message": f"Вы успешно подключились к семье с кодом {family.code}!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Метод для получения семьи по токену
    @action(detail=False, methods=['get'], url_path='retrieve-by-token')
    def retrieve_by_token(self, request):
        token = request.query_params.get('token')  # Получаем токен из параметра запроса
        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Пытаемся декодировать токен и извлечь нужную информацию
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])  # Замените 'secret' на ваш секретный ключ
            user_id = payload.get('user_id')  # Или другой параметр, который вам нужен
            
            # Ищем семью по пользователю в members
            family = Family.objects.filter(members__id=user_id).first()  # Ищем семью по user_id
            if family:
                return Response({"family_code": family.code}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Family not found'}, status=status.HTTP_404_NOT_FOUND)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
