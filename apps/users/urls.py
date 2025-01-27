from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path
from django.contrib.auth import views as auth_views 
from apps.users.views import UserAPI


from django.urls import path
from . import views

# urlpatterns = [
#     path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
# ]


router = DefaultRouter()
router.register('users', UserAPI, 'api_users')

urlpatterns = [
    # регистрацуия
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # восстановленя пароля 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += router.urls