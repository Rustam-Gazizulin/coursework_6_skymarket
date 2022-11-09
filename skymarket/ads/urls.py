from django.urls import include, path

from rest_framework_nested import routers

from .views import AdViewSet

ad_router = routers.SimpleRouter()
ad_router.register('ads', AdViewSet, basename='ads')

urlpatterns = [
    path('', include(ad_router.urls)),
]
