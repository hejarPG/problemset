from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChapterViewSet, ProblemViewSet, SolutionViewSet, TagViewSet

router = DefaultRouter()
router.register('chapters', ChapterViewSet)
router.register('problems', ProblemViewSet)
router.register('solutions', SolutionViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 