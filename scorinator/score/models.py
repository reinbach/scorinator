from django.db import models
from project.models import Project


class ProjectScoreManager(models.Manager):
    def top(self, limit=10):
        return self.get_query_set()[0:limit]


class ProjectScore(models.Model):
    project = models.ForeignKey(Project)
    total_score = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = ProjectScoreManager()

    class Meta:
        ordering = ('total_score', )


class ScoreAttribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)


class ProjectScoreAttribute(models.Model):
    score_attribute = models.ForeignKey(ScoreAttribute)
    project_score = models.ForeignKey(ProjectScore)
    score_value = models.DecimalField(max_digits=8, decimal_places=2)
    result = models.TextField()
