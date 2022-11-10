from django.urls import include, path

from rest_framework_nested import routers

from .views import AdViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('ads', AdViewSet, basename='ads')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
