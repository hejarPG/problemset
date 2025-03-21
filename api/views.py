from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from problems.models import Chapter, Problem, Solution, Tag
from .serializers import ChapterSerializer, ProblemSerializer, SolutionSerializer, TagSerializer

# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['chapter', 'difficulty', 'tags']
    search_fields = ['title', 'statement']
    
    @action(detail=True, methods=['get'])
    def solution(self, request, pk=None):
        problem = self.get_object()
        try:
            solution = Solution.objects.get(problem=problem)
            serializer = SolutionSerializer(solution)
            return Response(serializer.data)
        except Solution.DoesNotExist:
            return Response({'detail': 'Solution not found'}, status=404)

class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
