from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class Problem(models.Model):
    title = models.CharField(max_length=200)
    statement = models.TextField()  # LaTeX content
    chapter = models.ForeignKey(Chapter, related_name='problems', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='problems', blank=True)
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['chapter__order']

class Solution(models.Model):
    problem = models.OneToOneField(Problem, related_name='solution', on_delete=models.CASCADE)
    content = models.TextField()  # LaTeX content
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Solution for {self.problem.title}"
