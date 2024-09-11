from django.shortcuts import render
from rest_framework import generics
from .models import Workout, Exercises, Measurements
from .serializers import WorkoutSerializer, ExercisesSerializer, MeasurementsSerializer

class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ExercisesListCreateView(generics.ListCreateAPIView):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class ExercisesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class MeasurementsListCreateView(generics.ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer


class MeasurementsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
