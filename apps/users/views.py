from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.users.serializers import UserRegisterSerializer
from apps.users.models import User



class UserAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserRegisterSerializer
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)