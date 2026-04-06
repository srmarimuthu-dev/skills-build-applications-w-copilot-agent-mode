from rest_framework import serializers
from .models import Activity, Team, TeamMember, WorkoutSuggestion
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id = serializers.CharField(source='_id', read_only=True)  # Convert ObjectId to string

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date', 'points']

class TeamSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_by', 'created_at']

class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = TeamMember
        fields = ['id', 'team', 'user', 'joined_at']

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'suggestion', 'created_at']