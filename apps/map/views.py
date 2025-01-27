from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Route
from .serializers import RouteSerializer

class RouteListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Получение данных из тела запроса
        start_location = request.query_params.get('start_location')
        end_location = request.query_params.get('end_location')
        waypoints = request.query_params.get('waypoints')
        comment = request.query_params.get('comment')
        additional_points = request.query_params.get('additional_points')


        # Проверка на обязательные параметры
        if not start_location or not end_location:
            return Response(
                {"error": "start_location и end_location — обязательные поля."},
                status=400
            )

        # Создание маршрута
        route = Route.objects.create(
            user=request.user,
            start_location=start_location,
            end_location=end_location,
            waypoints=waypoints,
            comment=comment,
            additional_points=additional_points,
        )

        # Сериализация и возврат ответа
        serializer = RouteSerializer(route)
        return Response(serializer.data, status=201)