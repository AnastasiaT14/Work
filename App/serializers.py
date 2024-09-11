from rest_framework import serializers
from .models import Workout, Exercises, Measurements


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = "__all__"


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = "__all__"
