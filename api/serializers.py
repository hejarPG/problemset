from rest_framework import serializers
from problems.models import Chapter, Problem, Solution, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['id', 'content', 'created_at', 'updated_at']

class ProblemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    solution = SolutionSerializer(read_only=True)
    
    class Meta:
        model = Problem
        fields = ['id', 'title', 'statement', 'chapter', 'tags', 'solution', 
                  'difficulty', 'created_at', 'updated_at']

class ChapterSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'description', 'order', 'problems'] 