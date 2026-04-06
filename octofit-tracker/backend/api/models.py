from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models

class Activity(djongo_models.Model):
    user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
    activity_type = djongo_models.CharField(max_length=100)
    duration = djongo_models.IntegerField()  # in minutes
    date = djongo_models.DateTimeField(auto_now_add=True)
    points = djongo_models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Team(djongo_models.Model):
    name = djongo_models.CharField(max_length=100)
    description = djongo_models.TextField(blank=True)
    created_by = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
    created_at = djongo_models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamMember(djongo_models.Model):
    team = djongo_models.ForeignKey(Team, on_delete=djongo_models.CASCADE)
    user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
    joined_at = djongo_models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('team', 'user')

    def __str__(self):
        return f"{self.user.username} in {self.team.name}"

class WorkoutSuggestion(djongo_models.Model):
    user = djongo_models.ForeignKey(User, on_delete=djongo_models.CASCADE)
    suggestion = djongo_models.TextField()
    created_at = djongo_models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion for {self.user.username}"