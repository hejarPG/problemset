from django.contrib import admin
from .models import Chapter, Problem, Solution, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    ordering = ('order',)

class SolutionInline(admin.StackedInline):
    model = Solution
    extra = 1

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'difficulty', 'created_at')
    list_filter = ('chapter', 'difficulty', 'tags')
    search_fields = ('title', 'statement')
    inlines = [SolutionInline]
    filter_horizontal = ('tags',)

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('problem', 'updated_at')
    search_fields = ('problem__title', 'content')
