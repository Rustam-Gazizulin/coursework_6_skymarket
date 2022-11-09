from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views


users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path("token/", views.TokenObtainPairView.as_view(), name='token_obtain'),
    path("refresh/", views.TokenRefreshView.as_view(), name='token_refresh'),
]
