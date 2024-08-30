from django.shortcuts import render
from rest_framework import generics
from .models import Application, Measurements
from .serializers import ApplicationSerializer, MeasurementsSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class MeasurementsListCreateView(generics.ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer


class MeasurementsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
